===============================================================
Deploying AtlanticWave-SDX into multiple servers
===============================================================

Introduction
============

This page list the steps necessary for building the AW-SDX whole environment
into multiple servers, also using Docker and Docker-compose on each one of them.


The following table ilustrates roles and responsabilities for the multiple servers.
IP addresses there are just for ilustration, your setup can use
different addresses, as long as you adapt the configs throughout
this guide.

+----------------+----------------+---------------------------+
| Server         | IP address     | Description               |
+================+================+===========================+
| sdx-controller | 192.168.56.104 | Runs SDX-Controller:      |
|                |                |  - sdx-controller         |
|                |                |  - Mongo                  |
|                |                |  - RabbitMQ               |
|                |                |  - Mininet                |
+----------------+----------------+---------------------------+
| meican         | 192.168.56.105 | runs Meican system        |
+----------------+----------------+---------------------------+
| oxp-ampath     | 192.168.56.100 | Runs Amlight/AMPATH OXP:  |
|                |                |  - Kytos                  |
|                |                |  - SDX-LC                 |
|                |                |  - Mongo                  |
+----------------+----------------+---------------------------+
| oxp-sax        | 192.168.56.102 | Runs SAX OXP:             |
|                |                |  - Kytos                  |
|                |                |  - SDX-LC                 |
|                |                |  - Mongo                  |
+----------------+----------------+---------------------------+
| oxp-tenet      | 192.168.56.103 | Runs Tenet OXP:           |
|                |                |  - Kytos                  |
|                |                |  - SDX-LC                 |
|                |                |  - Mongo                  |
+----------------+----------------+---------------------------+

Note that Mininet was deployed on the sdx-controller just for
simplicity, but it is okay if you decide to have a separed server
only for that. Another approach would be run mininet on each OXP
and the leverage VXLAN or L2TP to create inter-domain links.

Note also that RabbitMQ was created on sdx-controller for simplicity.
It can also be created on a separated server.

All build process will be based on **main** branches.

Pre-requirements
================

In order to be able to run this step-by-step, you need to have:

- All vms above created and running. For the setup documented here,
  Debian 11 was utilized
- Docker installed each server (https://docs.docker.com/engine/install/debian/)
- Servers should have proper firewall rules in place to allow communication,
  specially the following ports
  - RabbitMQ between oxp-ampath/oxp-sax/oxp-tenet and sdx-controller (port 5672/tcp)
  - OpenFlow between oxp-ampath/oxp-sax/oxp-tenet and Mininet (sdx-controller) (6653/tcp)
  - HTTP between sdx-controller and Meican (8080/tcp)

Deploying SDX-Controller
========================

1. Create an instance for RabbitMQ:

.. code-block :: RST

	docker run -d --name mq1 --pull always -e RABBITMQ_DEFAULT_USER=testsdx1 -e RABBITMQ_DEFAULT_PASS=testsdx1 -p 5672:5672 rabbitmq:latest

2. Create an instance for MongoDB and configure a database/username/password:

.. code-block :: RST

	docker run -d --name mongo --pull always mongo:7.0
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("sdxctl").createUser({user: "sdxctl", pwd: "sdxctl", roles: [ { role: "dbAdmin", db: "sdxctl" } ]})'

3. Install dependencies and build sdx-controller:

.. code-block :: RST

	sudo apt-get  install -y git vim jq
	git clone https://github.com/atlanticwave-sdx/sdx-controller
	cd sdx-controller
	docker build -t sdx-controller .

4. Create an instance for sdx-controller based on a set of environment variables:

.. code-block :: RST

	cat >sdx-controller.env <<EOF
	MONGODB_CONNSTRING=mongodb://sdxctl:sdxctl@mongo:27017/sdxctl
	DB_NAME=sdxctl
	DB_CONFIG_TABLE_NAME=sdxctl_table
	SUB_QUEUE=topo
	MQ_HOST=192.168.56.104
	MQ_PORT=5672
	MQ_USER=testsdx1
	MQ_PASS=testsdx1
	EOF
	
	docker run -d --name sdx-controller --link mongo --env-file sdx-controller.env -p 8080:8080 sdx-controller:latest

5. Create an instance for Mininet point to the OXPO that will be created later on:

.. code-block :: RST

	curl -LO https://raw.githubusercontent.com/atlanticwave-sdx/sdx-continuous-development/main/data-plane/container-mininet/link-hosts.py
	sed -i '1s/python/python3/g' link-hosts.py
	docker run --pull always -d --name mininet -it --privileged -v /lib/modules:/lib/modules -v ./link-hosts.py:/link-hosts.py italovalcy/mininet:latest file:///link-hosts.py 192.168.56.100 192.168.56.102 192.168.56.103

Deploying OXP-Ampath
========================

1. Create an instance for Mongo along with database/username/password for Kytos and SDX-LC:

.. code-block :: RST

	docker run --pull always -d --name mongo mongo:7.0
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("amlight").createUser({user: "amlight", pwd: "amlight", roles: [ { role: "dbAdmin", db: "amlight" } ]})'
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("sdx_lc").createUser({user: "sdxlcmongo_user", pwd: "sdxlcmongo_pw", roles: [ { role: "dbAdmin", db: "sdx_lc" } ]})'

2. Install dependencies and build Kytos-ng OXPO:

.. code-block :: RST

	sudo apt-get  install -y git vim jq
	git clone https://github.com/atlanticwave-sdx/kytos-sdx
	cd kytos-sdx
	docker build --pull -t kytos-sdx .

3. Create an instance for Kytos-ng OXPO based on a set of environment variables:

.. code-block :: RST

	cat >kytos-sdx.env <<EOF
	MONGO_HOST_SEEDS=mongo:27017
	MONGO_DBNAME=amlight
	MONGO_USERNAME=amlight
	MONGO_PASSWORD=amlight
	SDXLC_URL=http://192.168.56.100:8080/SDX-LC/2.0.0/topology
	OXPO_NAME=Ampath-OXP
	OXPO_URL=ampath.net
	EOF

	docker run  --name ampath-kytos -d --init -p 8181:8181 -p 6653:6653 --link mongo --env-file kytos-sdx.env kytos-sdx:latest

4. Build and create the SDX-LC container:

.. code-block :: RST

	sudo apt-get  install git
	git clone https://github.com/atlanticwave-sdx/sdx-lc
	cd sdx-lc/
	docker build -t sdx-lc .
	
	cat >amlight-sdx-lc.env <<EOF
	SDXLC_PORT=8080
	MONGODB_CONNSTRING=mongodb://sdxlcmongo_user:sdxlcmongo_pw@mongo:27017/sdx_lc
	OXP_CONNECTION_URL=http://192.168.56.100:8181/api/kytos/sdx/v1/l2vpn_ptp
	DB_NAME=sdx_lc
	DB_CONFIG_TABLE_NAME=ampath_sdx_lc
	OXP_PULL_URL=http://192.168.56.100:8181/api/kytos/sdx/topology/2.0.0
	OXP_PULL_INTERVAL=180
	SDXLC_DOMAIN=ampath.net
	SUB_QUEUE=connection
	MQ_HOST=192.168.56.104
	MQ_PORT=5672
	MQ_USER=testsdx1
	MQ_PASS=testsdx1
	EOF
	
	docker run -d --name ampath-sdx-lc --link mongo --env-file amlight-sdx-lc.env -p 8080:8080 sdx-lc:latest

Deploying OXP-SAX
========================

1. Create an instance for Mongo along with database/username/password for Kytos and SDX-LC:

.. code-block :: RST

	docker run --pull always -d --name mongo mongo:7.0
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("sax").createUser({user: "sax", pwd: "sax", roles: [ { role: "dbAdmin", db: "sax" } ]})'
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("sdx_lc").createUser({user: "sdxlcmongo_user", pwd: "sdxlcmongo_pw", roles: [ { role: "dbAdmin", db: "sdx_lc" } ]})'

2. Install dependencies and build Kytos-ng OXPO:

.. code-block :: RST

	sudo apt-get  install -y git vim jq
	git clone https://github.com/atlanticwave-sdx/kytos-sdx
	cd kytos-sdx
	docker build --pull -t kytos-sdx .

3. Create an instance for Kytos-ng OXPO based on a set of environment variables:

.. code-block :: RST

	cat >kytos-sdx.env <<EOF
	MONGO_HOST_SEEDS=mongo:27017
	MONGO_DBNAME=sax
	MONGO_USERNAME=sax
	MONGO_PASSWORD=sax
	SDXLC_URL=http://192.168.56.102:8080/SDX-LC/2.0.0/topology
	OXPO_NAME=SAX-OXP
	OXPO_URL=sax.net
	EOF

	docker run  --name sax-kytos -d --init -p 8181:8181 -p 6653:6653 --link mongo --env-file kytos-sdx.env kytos-sdx:latest

4. Build and create the SDX-LC container:

.. code-block :: RST

	sudo apt-get  install git
	git clone https://github.com/atlanticwave-sdx/sdx-lc
	cd sdx-lc/
	docker build -t sdx-lc .

	cat >sax-sdx-lc.env <<EOF
	SDXLC_PORT=8080
	MONGODB_CONNSTRING=mongodb://sdxlcmongo_user:sdxlcmongo_pw@mongo:27017/sdx_lc
	OXP_CONNECTION_URL=http://192.168.56.102:8181/api/kytos/sdx/v1/l2vpn_ptp
	DB_NAME=sdx_lc
	DB_CONFIG_TABLE_NAME=sax_sdx_lc
	OXP_PULL_URL=http://192.168.56.102:8181/api/kytos/sdx/topology/2.0.0
	OXP_PULL_INTERVAL=180
	SDXLC_DOMAIN=sax.net
	SUB_QUEUE=connection
	MQ_HOST=192.168.56.104
	MQ_PORT=5672
	MQ_USER=testsdx1
	MQ_PASS=testsdx1
	EOF
	
	docker run -d --name sax-sdx-lc --link mongo --env-file sax-sdx-lc.env -p 8080:8080 sdx-lc:latest

Deploying OXP-Tenet
========================

1. Create an instance for Mongo along with database/username/password for Kytos and SDX-LC:

.. code-block :: RST

	docker run --pull always -d --name mongo mongo:7.0
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("tenet").createUser({user: "tenet", pwd: "tenet", roles: [ { role: "dbAdmin", db: "tenet" } ]})'
	docker exec -it mongo mongosh --eval 'db.getSiblingDB("sdx_lc").createUser({user: "sdxlcmongo_user", pwd: "sdxlcmongo_pw", roles: [ { role: "dbAdmin", db: "sdx_lc" } ]})'

2. Install dependencies and build Kytos-ng OXPO:

.. code-block :: RST

	sudo apt-get  install -y git vim jq
	git clone https://github.com/atlanticwave-sdx/kytos-sdx
	cd kytos-sdx
	docker build --pull -t kytos-sdx .

3. Create an instance for Kytos-ng OXPO based on a set of environment variables:

.. code-block :: RST

	cat >kytos-sdx.env <<EOF
	MONGO_HOST_SEEDS=mongo:27017
	MONGO_DBNAME=tenet
	MONGO_USERNAME=tenet
	MONGO_PASSWORD=tenet
	SDXLC_URL=http://192.168.56.103:8080/SDX-LC/2.0.0/topology
	OXPO_NAME=Tenet-OXP
	OXPO_URL=tenet.ac.za
	EOF

	docker run  --name tenet-kytos -d --init -p 8181:8181 -p 6653:6653 --link mongo --env-file kytos-sdx.env kytos-sdx:latest

4. Build and create the SDX-LC container:

.. code-block :: RST

	sudo apt-get  install git
	git clone https://github.com/atlanticwave-sdx/sdx-lc
	cd sdx-lc/
	docker build -t sdx-lc .

	cat >tenet-sdx-lc.env <<EOF
	SDXLC_PORT=8080
	MONGODB_CONNSTRING=mongodb://sdxlcmongo_user:sdxlcmongo_pw@mongo:27017/sdx_lc
	OXP_CONNECTION_URL=http://192.168.56.103:8181/api/kytos/sdx/v1/l2vpn_ptp
	DB_NAME=sdx_lc
	DB_CONFIG_TABLE_NAME=tenet_sdx_lc
	OXP_PULL_URL=http://192.168.56.103:8181/api/kytos/sdx/topology/2.0.0
	OXP_PULL_INTERVAL=180
	SDXLC_DOMAIN=tenet.ac.za
	SUB_QUEUE=connection
	MQ_HOST=192.168.56.104
	MQ_PORT=5672
	MQ_USER=testsdx1
	MQ_PASS=testsdx1
	EOF
	
	docker run -d --name tenet-sdx-lc --link mongo --env-file tenet-sdx-lc.env -p 8080:8080 sdx-lc:latest

Final config on SDX-Controller
==============================

- Configure the OXPs to enable switches, interfaces and links, as well as enable Kytos-SDX-Topology to send the topology to SDX-LC:

.. code-block :: RST

	curl -LO https://raw.githubusercontent.com/atlanticwave-sdx/sdx-continuous-development/main/data-plane/scripts/curl/2.enable_all.sh
	sed -i 's/0.0.0.0:8181/192.168.56.100:8181/g' 2.enable_all.sh
	sed -i 's/0.0.0.0:8282/192.168.56.102:8181/g' 2.enable_all.sh
	sed -i 's/0.0.0.0:8383/192.168.56.103:8181/g' 2.enable_all.sh
	bash 2.enable_all.sh
	

- At this point the SDX-LC will pull the topology from OXPO (Kytos-ng) periodically on each OXP. You can force the OXPO to push the topology to SDX-LC by running the following command:

.. code-block :: RST

	curl -s -X POST http://192.168.56.100:8181/api/kytos/sdx/topology/2.0.0
	curl -s -X POST http://192.168.56.102:8181/api/kytos/sdx/topology/2.0.0
	curl -s -X POST http://192.168.56.103:8181/api/kytos/sdx/topology/2.0.0

- Check if the Nodes, and Links were loaded to SDX-Controller:

.. code-block :: RST

	curl -s http://192.168.56.104:8080/SDX-Controller/topology | jq -r '.nodes[] | (.ports[] | .id)'
	curl -s http://192.168.56.104:8080/SDX-Controller/topology | jq -r '.links[] | .id + " " + .ports[0] + " " + .ports[1]'

- Create a connection:

.. code-block :: RST

	curl -s -X POST -H 'Content-type: application/json' http://0.0.0.0:8080/SDX-Controller/l2vpn/1.0 -d '{"name": "VLAN between AMPATH/300 and TENET/300", "endpoints": [{"port_id": "urn:sdx:port:ampath.net:Ampath3:50", "vlan": "300"}, {"port_id": "urn:sdx:port:tenet.ac.za:Tenet03:50", "vlan": "300"}]}'

- List the breakouts created on the OXPs:

.. code-block :: RST

	sdx-controller:~$ curl -s http://192.168.56.100:8181/api/kytos/mef_eline/v2/evc/ | jq -r '.[] | .id + " " + .name + " active=" + (.active|tostring)'
	73eb822faf6745 AMPATH_vlan_100_4095 active=true
	
	sdx-controller:~$ curl -s http://192.168.56.102:8181/api/kytos/mef_eline/v2/evc/ | jq -r '.[] | .id + " " + .name + " active=" + (.active|tostring)'
	089d976599a44e SAX_vlan_4095_4095 active=true
	
	sdx-controller:~$ curl -s http://192.168.56.103:8181/api/kytos/mef_eline/v2/evc/ | jq -r '.[] | .id + " " + .name + " active=" + (.active|tostring)'
	0050f201917949 TENET_vlan_4095_100 active=true

Meican
=======

1. The next step will be bringing SDX-Meican UP and integrate it with SDX-Controller. To do that, execute the following steps:

.. code-block :: RST

	cd ~
	git clone https://github.com/atlanticwave-sdx/sdx-meican
	cd sdx-meican

2. Adjust some configs on Meican's `.env` file to comply with your environment:

.. code-block :: RST

	vim .env

Some of the parameters you might want to change:

- **ORCID_CLIENT_ID**: Client ID and Client Secret must be obtained from ORCID (following the instructions in https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/). Example: `APP-S7XXXXXXXXXXXXXX`
- **ORCID_CLIENT_SECRET**: same here, this have to be obtained from ORCID. Example: `bbxxxxxx-9x0x-4xx1-xxxx-xxxxxxxxxxxxxx`
- **MEICAN_HOST**:  This will be the IP address of the meican host, or DNS. Typically, you can insert here the IP address of the host where you are running docker. You can use a IP address but using the DNS name makes it easy for ORCID registration, where you have to provide the URL (IP address can change, while DNS name will remain the same). Example: `192.168.56.104`
- **SDX_CONTROLLER_URL**: This will be the URL of the SDX-Controller. Since we are running everything on the same machine, you just provide here the IP address of the host where docker is running formated to the sdx-controller URL. Example: `http://192.168.56.104:8080/SDX-Controller/1.0.0/`

3. Build Meican:

.. code-block :: RST

	docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
