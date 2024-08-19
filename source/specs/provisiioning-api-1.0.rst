=======================================================================
AtlanticWave-SDX 2.0: Service Provisioning Data Model Specification 1.0
=======================================================================

Versioning
==========

+-----------------------+-----------------------+-----------------------+
| Version               | Date                  | Description           |
+=======================+=======================+=======================+
| 1.0                   | 06/19/2024            | Creates the           |
|                       |                       | Provisioning API and  |
|                       |                       | Data Model            |
|                       |                       | specification.        |
+-----------------------+-----------------------+-----------------------+

Introduction
============

The AtlanticWave-SDX 2.0 *Controller* (a.k.a. SDX Controller) is the
inter-domain service orchestrator component and primary interface for
users and science workflows in the AtlanticWave-SDX framework. Via the
SDX Controller’s user interface or API (a.k.a. application programming
interface), researchers, network operators, science experiments, and
scientific workflows can submit requests for AtlanticWave-SDX Services.
This document, *the AtlanticWave-SDX 2.0: Service Provisioning Data
Model Specification,* guides external users and software developers on
the service provisioning data model supported by the SDX Controller and
its operation.

Version 1.0 of the *AtlanticWave-SDX 2.0: Service Provisioning Data
Model Specification* focuses on the creation, editing, listing, and
deletion of intra- and inter-domain Layer 2 VPNs. This specification
will be used by end users, such as researchers and network operators,
scientific workflows, such as Chameleon and FABRIC, and science user
interfaces, such as MEICAN and AutoGOLE/SENSE.

The AtlanticWave-SDX 2.0 Controller’s API is based on REST
(REpresentational State Transfer) [1]_, a wildly popular API compatible
with the OpenAPI [2]_ initiative.

This specification is organized to enable additions as needed. The
document’s structure uses the following format:

-  | First, the SDX Service(s) supported are described, including their
     data models. For version 1.0, only L2VPN services are supported.

-  Second, a message body and return codes explain the SDX API actions.

   Note: This specification could also guide the communication between
   the SDX Controller and OXP orchestrators via SDX-LC, even though it
   primarily focuses on the interface between a user (researcher,
   network operator, science workflow) and the OXP orchestrator.

Requirement Levels
==================

To avoid confusion and misinterpretation, the keywords “must,” “must
not,” “required,” “shall,” “shall not,” “should,” “should not,”
“recommended,” “may,” and “optional” in this document are to be
interpreted as described in IETF RFC 2119
[https://www.ietf.org/rfc/rfc2119.txt].

SDX Services
============

Layer 2 Virtual Private Network / L2VPN
---------------------------------------

Layer 2 Virtual Private Network or L2VPN is an Ethernet service offered
by network operators to transport frames based on a unique VLAN
identifier connecting two or more endpoints. There are several
definitions to characterize an L2VPN in the scope of the
AtlanticWave-SDX 2.0 project:

1. A L2VPN could be **intra-domain** when endpoints are located and
   operated by the same open exchange point (OXP), or **inter-domain**
   when endpoints are located and operated by different OXPs.
2. A L2VPN could be **point-to-point** (or P2P) when there are only two
   endpoints or **point-to-multipoint** (P2MP) when there are more than
   two endpoints.
3. A L2VPN might have a bandwidth requirement, when a minimum bandwidth
   must be guaranteed by OXPs, or *best-effort*, which means that OXPs
   won’t provide special treatment or prioritization to the L2VPN’s
   frames.
4. A L2VPN might be needed just temporarily, with specific start and end
   times, or permanent, when the L2VPN must be supported indefinitely
   until its creator/owner deletes it.
5. A L2VPN might have a latency requirement, when a maximum latency must
   be addressed by the SDX Controller.
6. A L2VPN might have different VLAN IDs at the endpoints, meaning that
   the SDX Controller must perform a VLAN translation along the path.

There are several attributes that must be considered by users when
requesting a SDX L2VPN via the SDX Controller’s API. The L2VPN
attributes, such as name, endpoints, or bandwidth requirements, are
presented in the **Data Models** section.

Data Models
===========

Layer 2 Virtual Private Network - L2VPN
---------------------------------------

A L2VPN could have dozens of attributes based on user, Open Exchange
Point (OXP), and science needs. This specification defines a minimum
scope with primary attributes focusing on intra- and inter-domain
provisioning. Future specifications are encouraged to expand the list of
attributes supported.

| **Note:**
| In the *AtlanticWave-SDX 2.0 Service Provisioning Specification
  version 1.0* (this document), the data model is the same for both
  point-to-point and point-to-multipoint L2VPNs. When a service
  provisioning request is submitted by a SDX user, the SDX Controller
  must confirm that the OXP orchestrators involved have advertised
  support for the specific service (point-to-point or
  point-to-multipoint) in the Topology attribute named “**services**”.
  An error code is defined when incompatibility is observed. For more
  details of how OXPs can advertise SDX services, please refer to the
  `AtlanticWave-SDX 2.0 Topology Data Model
  specification <https://docs.google.com/document/d/1lgxjIT144EFu1G_OVcU19hN1cSUT_v2-tE0Z-7UlkNg/edit?usp=sharing>`__.

Mandatory Attributes
^^^^^^^^^^^^^^^^^^^^

For version 1.0, the SDX L2VPN service has the following **MANDATORY**
attributes: attributes that *must* be provided and non-empty, by the SDX
user when submitting a request for the creation of a SDX L2VPN service:

-  **name**. The attribute **name** is a string to label the L2VPN,
   defined by the SDX user. The **name** attribute is used by OXP and
   SDX operators to have a minimum description of the purpose of the
   L2VPN. The **name** attribute must be limited to 50 characters.

-  **endpoints**. The **endpoints** attribute is used to describe the
   endpoints of the L2VPN. The **endpoints** attribute must have two
   (P2P L2VPN) or more (P2MP L2VPN) entries, where each entry has one
   network interface [3]_ (a **Port** in the Topology Data Model
   Specification) plus a VLAN definition. The **endpoints** attribute is
   represented as a list of dictionaries [4]_. Each dictionary must have
   the following attributes:

   -  **port_id**: the **port_id** attribute is the URN (Uniform
      Resource Name) of a network device’s Port, following the
      `AtlanticWave-SDX Topology Data Model
      Specification <https://docs.google.com/document/d/1lgxjIT144EFu1G_OVcU19hN1cSUT_v2-tE0Z-7UlkNg/edit?usp=sharing>`__.
   -  **vlan**: the **VLAN** attribute describes how the SDX and OXPs
      should treat L2VPN frames with or without an IEEE 802.1Q
      Ethertype. The values accepted are:

      -  A string with a number/integer, for instance, **“50”**: When a
         user provides the **VLAN** attribute with an integer value, the
         user wants to transport only packets with the VLAN ID provided
         as the number. For instance, *{“vlan”: “50”}* means that the
         user wants only Ethernet frames with VLAN ID 50 to be
         transported by the L2VPN. This is the most common option.
      -  **“any”**: When a user requests the **vlan** attribute with the
         value “any,” the SDX Controller must choose a VLAN ID available
         based on the topology’s network interface’s attribute named
         **vlan_range**, represented by the **port_id**. This option is
         useful for situations where the user does not require a
         specific VLAN ID and delegates the responsibility to the SDX
         Controller.
      -  **“untagged”**: When a user provides the **vlan** attribute
         with value being the string **“untagged”**, it means that the
         user wants a L2VPN that only transports the Ethernet frames
         that have no IEEE 802.1Q Ethertype, known as “access mode” by
         some vendors.
      -  **VLAN range**: “VLAN ID1:VLAN ID2”. When a user provides the
         **vlan** attribute with the value being an integer, a colon,
         and another integer (for instance, “50:55”), it means that the
         user is asking for a range of VLANs to be transported by the
         L2VPN. This option is helpful for situations where the user
         needs to transport multiple VLANs between endpoints, and all
         VLAN IDs that must be transported are well-known by the SDX
         user. The VLAN ID values provided represent the first and the
         last VLAN in the range and they are included. For instance,
         “50:55” means that the SDX L2VPN must transport frames with
         VLAN IDs 50, 51, 52, 53, 54, and 55.
      -  **“all”**: When a SDX user provides the **vlan** attribute with
         the value being the string **“all,”** it means that the user
         wants to encapsulate all Ethernet frames with and without the
         IEEE 802.Q Ethertype coming from interface **port_id**. This
         option is useful for situations where the user needs to
         transport multiple VLANs between endpoints without having to
         track specific VLAN IDs.
      -  The **vlan** attribute’s values above have the following
         constraints:

         -  If one endpoint has the *VLAN range* or option “\ **all”**,
            all endpoints must have the same value.
         -  If one endpoint has the option “**any**”, the SDX Controller
            can choose any VLAN for that endpoint, even if the other(s)
            endpoint(s) are not configured as “**any**”.
         -  When one endpoint has the VLAN range option in use, all
            other endpoint(s) must have the same VLAN range.
         -  Only numbers from 1 to 4095 are supported as VLAN IDs.
         -  VLAN IDs must be integers provided as strings.

Below are some examples to create L2VPNs:

-  P2P with VLAN translation: VLAN ID 300 at AMPATH and VLAN ID 150 at
   TENET”

.. code-block::

   {
     "name": "VLAN between AMPATH/300 and TENET/150",
     "endpoints": [
       {"port_id": "urn:sdx:port:tenet.ac.za:Tenet03:50", "vlan": "150"},
       {"port_id": "urn:sdx:port:ampath.net:Ampath3:50", "vlan": "300"}
     ]
   }

-  P2MP: VLAN ID 300 at AMPATH, TENET, at SAX”

.. code-block::

   {
     "name": "P2MP: VLAN ID 300 at AMPATH, TENET, at SAX",
     "endpoints": [
       {"port_id": "urn:sdx:port:tenet.ac.za:Tenet03:50", "vlan": "300"},
       {"port_id": "urn:sdx:port:sax.br:router_01:50", "vlan": "300"},
       {"port_id": "urn:sdx:port:ampath.net:Ampath3:50", "vlan": "300"}
     ]
   }

-  P2P with option “any”: VLAN ID 59 at AMPATH and any VLAN ID at TENET”

.. code-block::

   {
     "name": "VLAN between AMPATH/59 and TENET/any",
     "endpoints": [
       {"port_id": "urn:sdx:port:tenet.ac.za:router_03:5", "vlan": "any"},
       {"port_id": "urn:sdx:port:ampath.net:mia-mi1-sw01:5", "vlan": "59"}
     ]
   }

-  P2P with VLAN range: VLAN range 10-99 at AMPATH and at SAX”

.. code-block::

   {
     "name": "VLANs 10-99 between AMPATH and SAX",
     "endpoints": [
       {"port_id": "urn:sdx:port:sax.br:rtr_03:eth1", "vlan": "10:99"},
       {"port_id": "urn:sdx:port:ampath.net:sw01:5", "vlan": "10:99"}
     ]
   }

-  P2P with untagged and a VLAN ID: VLAN ID 10 at AMPATH and untagged at
   SAX”

.. code-block::

   {
     "name": "VLAN between AMPATH/10 and SAX/untagged",
     "endpoints": [
       {"port_id": "urn:sdx:port:sax.br:rtr_03:eth2", "vlan": "untagged"},
       {"port_id": "urn:sdx:port:ampath.net:sw01:40", "vlan": "10"}
     ]
   }

Optional Attributes
^^^^^^^^^^^^^^^^^^^

For version 1.0, the SDX L2VPN service has the following **OPTIONAL**
attributes, attributes that *might* be provided by the SDX user when
submitting a request for the creation of a SDX L2VPN service:

-  **description**. The **description** attribute is a user-defined
   field that gives details to the SDX operator about the L2VPN’s
   purpose for future reporting. The description could be a statement or
   a URL. This field must be limited to 255 characters.

-  **notifications**. The **notifications** attribute is a list of
   destinations for the SDX user to be notified in case of issues or
   changes with its SDX service. Each entry is a dictionary with the key
   “email” and value being one e-mail address destination. The SDX user
   can provide up to 10 (ten) e-mail addresses.

-  **scheduling**. The **scheduling** attribute is used to enable the
   SDX user with the ability to define a start time and/or end time for
   its SDX service. The **scheduling** attribute is a dictionary with
   two possible keys: **start_time** and **end_time**. The following
   conditions apply to the **scheduling** attribute:

   -  If the **start_time** attribute is not provided, it means that the
      SDX service must be provisioned immediately.
   -  If the **end_time** attribute is not provided, it means that the
      SDX service must not be scheduled to be removed.
   -  If the SDX user does not provide any attributes (the
      **scheduling** attribute is empty), the SDX Controller must treat
      the request as to be provisioned immediately and never scheduled
      to be removed.
   -  ISO8601 must be used to represent the desired date and time,
      following the same format specified by the `AtlanticWave-SDX 2.0
      Topology Data Model
      specification <https://docs.google.com/document/d/1lgxjIT144EFu1G_OVcU19hN1cSUT_v2-tE0Z-7UlkNg/edit?usp=sharing>`__.
   -  The **end_time** attribute, when present, must be greater than the
      **start_time**, when also present, otherwise the standard HTTP 400
      error code must be sent back to the user.

-  **qos_metrics**. The **qos_metrics** attribute is used to enable the
   SDX user to provide network requirements/conditions for the SDX
   service to be deployed. These requirements are focused on the Quality
   of Service (QoS) characteristics of the SDX service.

   -  The **qos_metrics** attribute is a dictionary. Each of its keys
      (**min_bw**, **max_delay**, and **max_number_oxps)** has values as
      a dictionary. Each **qos_metrics** attribute’s key is a dictionary
      with two possible subkeys\ **: “value”** and **“strict”.**

      -  **value** is used by the user to indicate the metric value
         depending on the metrics: minimum bandwidth, maximum end-to-end
         delay, and maximum number of OXPs in the path.
      -  **strict** is used by the user to indicate if this metric is a
         deal-breaking metric. **strict** is a boolean value represented
         by **true** or **false**.

         -  In case **strict** has the value of **true**, if the SDX PCE
            doesn’t identify a path that can fulfill the user QoS
            requirements, then the standard HTTP 400 error code is sent
            back to the user and the SDX service is not created (if it
            is a service creating request) or deactivated (if it is an
            service editing/changing request). (Note: Creating, Editing
            and Changing actions will be discussed in the Actions
            section).
         -  In case **strict** has the value of **false,** the SDX
            Controller will create or edit the SDX service even if the
            SDX PCE doesn’t identify a path as requested.
         -  If the key **strict** is not provided, the SDX Controller
            will consider it as **false**.

   -  The **qos_metrics** attribute accepts the following
      sub-attributes:

      -  **min_bw**: The **min_bw** sub-attribute describes the
         bandwidth available (residual bandwidth [5]_) for the end to
         end path. When requesting a minimum bandwidth for the SDX
         service, the subkey “**value**” under “**min_bw**” must be
         provided as an integer from 0 to 100 representing the bandwidth
         in gigabits per second. For instance, if the minimum bandwidth
         expected is 20Gbps, the SDX user must set the subkey
         “\ **value”** with value of 20:

         .. code-block::

           {"min_bw": {"value": 20 }}

         or:

         .. code-block::

           {"min_bw": {"value": 20, "strict": false }}

         or:

         .. code-block::

           {"min_bw": {"value": 20, "strict": true }}


      -  **max_delay:** The **max_delay** sub-attribute describes the
         total delay acceptable for the path in milliseconds between the
         two endpoints for point-to-point services or between each pair
         of endpoints for point-to-multipoint. When requesting a maximum
         delay for the SDX service, the subkey “**value**” under
         **max_delay** must be provided as an integer from 0 to 1000
         with the value meaning the delay in milliseconds. For instance,
         if the maximum delay is 200 milliseconds, the SDX user must the
         set the subkey “**value**” with value of 200:

         .. code-block::

            {"max_delay": {"value": 200 }}

         or:

         .. code-block::

            {"max_delay": {"value": 200, "strict": false }}

         or:

         .. code-block::

            {"max_delay": {"value": 200, "strict": true }}


      -  **max_number_oxps:** The **max_number_oxps** sub-attribute
         describes the total number of OXPs in the path. When requesting
         a maximum number of OXPs in the path, the subkey “**value**”
         under **max_number_oxps** must be provided as an integer from 1
         to 100. For instance, if the maximum number of OXPs in the path
         is 4, the SDX user must the set the subkey “**value**” with
         value of 4:

         .. code-block::

            {"max_number_oxps": {"value": 4 }}

         or:

         .. code-block::

            {"max_number_oxps": {"value": 4, "strict": false }}

         or:

         .. code-block::

            {"max_number_oxps": {"value": 4, "strict": true }}

   Attention: From the AtlanticWave-SDX 2.0 perspective, these QoS
   metrics will be used by the SDX PCE (Path Computation Element) to
   find the ideal path. However, the AtlanticWave-SDX 2.0 framework
   can’t guarantee or enforce their implementation at the OXP level.

Below are two examples to create L2VPNs with optional attributes:

-  Example 1:

   -  VLAN ID 300 at AMPATH and VLAN ID 150 at TENET
   -  End time at December 31st, 2025, 12:00 PM UTC
   -  Optional/non-strict minimum bandwidth of 5 Gbps
   -  Strict max delay of 150 milliseconds
   -  Notifications to be sent to user@domain.com and user2@domain2.com

.. code-block::

   {
     "name": "VLAN between AMPATH/300 and TENET/150",
     "endpoints": [
       {"port_id": "urn:sdx:port:tenet.ac.za:Tenet03:50", "vlan": "150"},
       {"port_id": "urn:sdx:port:ampath.net:Ampath3:50", "vlan": "300"}
     ],
     "description": "This is an example to demonstrate a L2VPN with optional attributes",
     "scheduling": {
       "end_time": "2025-12-31T12:00:00Z"
     },
     "qos_metrics": {
       "min_bw": {
         "value": 5,
         "strict": false
       },
       "max_delay": {
         "value": 150,
         "strict": true
       }
     },
     "notifications": [
       {"email": "user@domain.com"},
       {"email": "user2@domain2.com"}
     ]
   }

-  Example 2:

   -  **Any** VLAN ID at AMPATH and SAX
   -  **Strict** max number of OXPs in the path of 3
   -  **Notifications** to be sent to user3@domain.com

.. code-block::

   {
     "name": "VLAN between AMPATH/Any and SAX/Any",
     "endpoints": [
       {"port_id": "urn:sdx:port:sax.br:Rtr01:50", "vlan": "any"},
       {"port_id": "urn:sdx:port:ampath.net:Ampath3:50", "vlan": "any"}
     ],
     "qos_metrics": {
       "max_number_oxps": {
         "value": 3,
         "strict": true
       }
     },
     "notifications": [
       {"email": "user3@domain.com"}
     ]
   }

Actions
=======

The Provisioning API and Data Model specification 1.0 supports four
actions: Creating a SDX L2VPN, Editing or Changing a SDX L2VPN, Listing
or Retrieving one or more SDX L2VPN(s), and Deleting a SDX L2VPN.

Following the OpenAPI standards, when submitting requests to the SDX
Controller, the request body (if any) must follow the JSON text
format [6]_. The SDX Controller will track the data model versioning via
API endpoint versions. The current data model version is 1.0.

Creating a SDX L2VPN
--------------------

Description
^^^^^^^^^^^

SDX users must be able to request new SDX L2VPNs via the SDX
Controller’s API. The endpoints (interface plus VLAN ID) must not be in
use by another L2VPN. The request and creation of L2VPNs via API must
operate asynchronously: the SDX user submits the JSON request body and
the SDX Controller provides back a service identifier (a.k.a. Service
ID) while working to provision the SDX service with all OXPs involved,
which might take several seconds.

This Service ID must follow the **Universally Unique Identifier**
(**UUID**) format. The Service ID (service_id) will be used to identify
the SDX L2VPN until it is deleted. The Service ID will be used by other
SDX components, such as the Behavior, Anomaly, and Performance Manager
(BAPM) when submitting the service counters and metrics.

SDX Internal Operation
''''''''''''''''''''''

Once a SDX L2VPN service is provisioned, the SDX Controller must add the
following attributes to the L2VPN. These attributes must be exported to
the SDX user when queries are submitted:

-  **service_id**: the service Universally Unique Identifier (UUID)
   returned to the user
-  **ownership**: a string representing the authenticated user or token
   that submitted the SDX Service request
-  **creation_date**: the service creation time using ISO860, following
   the same format specified by the AtlanticWave-SDX 2.0 Topology Data
   Model specification.
-  **archived_date**: When a user requests a SDX L2VPN to be deleted,
   the SDX Controller must populate this field with the datetime of the
   request. Initial value is 0.
-  **status**: represents the L2VPN’s current operational status.
   **status** is an enum [7]_ (or enumeration) with the following
   values: “up” if the L2VPN is operational, “down” if the L2VPN is not
   operational due to topology issues/lack of path, or endpoints being
   down, “error” when there is an error with the L2VPN, “under
   provisioning” when the L2VPN is still being provisioned by the OXPs,
   and “maintenance” when the L2VPN is being affected by a network
   maintenance.
-  **state**: represents the L2VPN’s current administrative state.
   **state** is an enum with the following values: “enabled” if the
   L2VPN is in administrative enable mode and “disabled” when the L2VPN
   is in administrative disable mode.
-  **counters_location**: the link to the Grafana page with the L2VPN
   counters.
-  **last_modified**: the datetime of the last modification performed on
   the L2VPN. Initial value is 0.
-  **current_path**: the URI of the interdomain links in the path
   following the `AtlanticWave-SDX Topology Data Model
   Specification <https://docs.google.com/document/d/1lgxjIT144EFu1G_OVcU19hN1cSUT_v2-tE0Z-7UlkNg/edit?usp=sharing>`__.
   The internal OXP topology must NOT be provided, only the links
   between OXPs.
-  **oxp_service_ids**: list of the OXPs’ service_ids for the OXP’s
   service. This field will be used to enable the *Editing/Changing*
   functionality described in the next section.

This **oxp_service_ids** attribute is a key attribute to be managed by
the SDX Controller. Using the per-OXP service ID(s), the SDX Controller
will support editing/changing the SDX L2VPN in the future as per user
needs. For instance, if a SDX user changes the SDX L2VPN endpoints, when
passing the new endpoints to one or more OXP orchestrators involved, the
OXP’s **service_id** will need to be provided to avoid overlaps and
mistakes by OXP orchestrators. The **oxp_service_ids** attribute’s
format is a dictionary with keys being the OXPs’ URL as described in the
AtlanticWave-SDX Topology Data Model specification. The value for each
key is a list with the service ID(s) received from the OXP orchestrator.
Having the value as a list will enable support for VLAN ranges and
point-to-multipoint L2VPNs. For example, consider a point-to-point L2VPN
that goes from AmLight.net to Tenet.ac.za via SAX.br. Each OXP provided
its own **service_id** as below:

-  AmLight.net provided the service_id c73da8e1
-  TENET.ac.za provide the service_id 5d034620
-  SAX.br provided the service_id 7cdf23e8978c

Using the data above, the **oxp_service_ids** attribute would be
populated as:

.. code-block::

   "oxp_service_ids": {
     "AmLight.net": ["c73da8e1"],
     "TENET.ac.za": ["5d034620"],
     "SAX.br": ["7cdf23e8978c"]
   }

**Provisioning L2VPNs with VLAN range**: The AtlanticWave-SDX 2.0
Topology Data Model Specification 2.0 does not have an option for OXP
network orchestrators or the SDX Local Controllers to notify the SDX
Controller of OXP service capabilities. For instance, OXP network
orchestrators can’t notify the SDX Controller if they support VLAN
range. In that case, if a SDX user submits a request for a SDX L2VPN
with a VLAN range option, this specification *suggests* the following
approach:

1. The SDX L2VPN VLAN range is presented to the SDX user as a single SDX
   L2VPN service, with a single **service_id**.
2. For each VLAN in the VLAN range, a L2VPN is requested from the OXPs,
   called OXP L2VPNs. For instance, SDX L2VPN with VLAN range of 10:12
   becomes three OXP L2VPNs: OXP L2VPN for VLAN 10, OXP L2VPN for VLAN
   11, and OXP L2VPN for VLAN 12. Each OXP L2VPN has its own OXP’s
   service ID back.
3. The SDX L2VPN **oxp_service_ids** attribute will store, for each OXP,
   all OXP’s service IDs, following the same order of the VLAN range.
4. The SDX L2VPN service life cycle will consider the multiple OXP
   L2VPNs for any operation: **qos_metrics** has to be evaluated for
   each individual OXP L2VPN, editing the SDX L2VPN vlan range should
   propagate to all individual OXP L2VPNs, and deleting a SDX L2VPN vlan
   range should delete all OXP L2VPN.

Request Format
^^^^^^^^^^^^^^

.. code-block::

   POST /l2vpn/1.0 HTTP/1.1
   Content-Type: application/json
   
   <L2VPN data model attributes>

Return Codes
^^^^^^^^^^^^

| 201: L2VPN Service Created
| 400: Request does not have a valid JSON or body is
  incomplete/incorrect
| 401: Not Authorized
| 402: Request not compatible (For instance, when a L2VPN P2MP is
  requested but only L2VPN P2P is supported)
| 409: L2VPN Service already exists.
| 410: Can’t fulfill the strict QoS requirements
| 411: Scheduling not possible
| 422: Attribute not supported by the SDX-LC/OXPO

Return Body if Successful
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   {"service_id": <UUID> }


Return Body if NOT successful
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   {"description": "text description that would help the user identify the reason for failure."}


Editing/Changing a SDX L2VPN
----------------------------

.. _description-1:

Description
^^^^^^^^^^^

SDX users must be able to change attributes of existing SDX L2VPNs. A
SDX user must only be allowed to make changes to its own SDX services.
Authentication and authorization are outside of the scope of this
document. SDX users must be allowed to change any user attributes
described in the Data Models section and the internal L2VPN **state**
attribute. SDX users must use the previously provided service_id when
requesting a change.

.. _sdx-internal-operation-1:

SDX Internal Operation
''''''''''''''''''''''

Any modifications performed to a SDX L2VPN via API must be logged for
accountability. Deleted/Archived L2VPNs can’t be edited. The internal
attribute **last_modified** must be updated with the datetime using the
ISO8601 format. Internal attributes can be modified by the SDX
Controller to address the user request, such as, **current_path**,
**last_modified,** and **state**.

If a SDX user changes the L2VPN **state** attribute, for instance,
changing it from *enabled* to *disabled*, the SDX Controller must
immediately request the OXPs involved to remove any configuration
related to the SDX L2VPN. Notice that disabling a L2VPN is not a final
state and can be reversed. When a SDX user changes a disabled L2VPN
**state** attribute to *enabled*, the SDX Controller must immediately
request the OXPs involved to create the configuration needed to support
the L2VPN. As previously mentioned, for any operation on a L2VPN, the
SDX Controller must update the **last_modified** attribute and record
the changes for accountability (in a database or log file).

If a VLAN range was requested in the original SDX L2VPN service, changes
should be propagated to all OXP L2VPN VLANs when it applies.

.. _request-format-1:

Request Format
^^^^^^^^^^^^^^

.. code-block::

   PATCH /l2vpn/1.0/{service_id} HTTP/1.1
   Content-Type: application/json
   
   <L2VPN attributes>

.. _return-codes-1:

Return Codes
^^^^^^^^^^^^

| 201: L2VPN Service Modified
| 400: Request does not have a valid JSON or body is
  incomplete/incorrect
| 401: Not Authorized
| 402: Request not compatible (For instance, when a L2VPN P2MP is
  requested but only L2VPN P2P is supported)
| 404: L2VPN Service ID not found.
| 409: Conflicts with a different L2VPN
| 410: Can’t fulfill the strict QoS requirements
| 411: Scheduling not possible

Return Body in case of success
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

None

.. _return-body-if-not-successful-1:

Return Body if NOT successful
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   {"description": "text description that would help the user identify the reason for failure."}


Listing/Retrieving one SDX L2VPN
--------------------------------

.. _description-2:

Description
^^^^^^^^^^^

SDX users must be able to retrieve all the attributes of their SDX
services. This query should be based on the SDX L2VPN Service ID.

.. _sdx-internal-operation-2:

SDX Internal Operation
''''''''''''''''''''''

Archived L2VPNs are not returned when **service_id** is specified.

.. _request-format-2:

Request Format:
^^^^^^^^^^^^^^^

.. code-block::

   GET /l2vpn/1.0/{service_id} HTTP/1.1

No request body is needed. This specification assumes that any request
body provided must be ignored by the SDX Controller.

.. _return-codes-2:

Return Codes:
^^^^^^^^^^^^^

| 200: OK
| 401: Not Authorized
| 404: Service ID not found

Return Body:

The return body must be a dictionary, if the requested **service_id**
exists and the user is authorized to have access to it. Otherwise no
return body will be provided.

The content of the dictionary will be the **service_id** as the key and
the L2VPN will be provided as another dictionary. For example:

.. code-block::

   Request: GET /l2vpn/1.0/c73da8e1-5d03-4620-a1db-7cdf23e8978c
   Return Code: 200
   Return body:
   
   {
     "c73da8e1-5d03-4620-a1db-7cdf23e8978c": {
       "service_id": "c73da8e1-5d03-4620-a1db-7cdf23e8978c",
       "name": "VLAN between AMPATH/300 and TENET/150",
       "endpoints": [
         {"port_id": "urn:sdx:port:tenet.ac.za:Tenet03:50", "vlan": "150"},
         {"port_id": "urn:sdx:port:ampath.net:Ampath3:50", "vlan": "300"}
       ],
       "description": "This is an example to demonstrate a L2VPN with
       optional attributes",
         "qos_metrics": {
           "min_bw": {
             "value": 5,
             "strict": false
         },
         "max_delay": {
           "value": 150,
           "strict": true
         }
       },
       "notifications": [
         {"email": "user@domain.com"},
         {"email": "user2@domain2.com"}
       ],
       "ownership": "user1",
       "creation_date": "20240522T00:00:00Z",
       "archived_date": "0",
       "status": "up",
       "state": "enabled",
       "counters_location": "https://my.aw-sdx.net/l2vpn/7cdf23e8978c",
       "last_modified": "0",
       "current_path": ["urn:sdx:link:tenet.ac.za:LinkToAmpath"],
       "oxp_service_ids": {
         "ampath.net": ["c73da8e1"],
         "tenet.ac.za": ["5d034620"]
       }
     }
   }

Listing/Retrieving multiple SDX L2VPNs
--------------------------------------

.. _description-3:

Description
^^^^^^^^^^^

SDX users must be able to retrieve all attributes of all SDX services
they own. This query is not based on SDX Service IDs.

.. _request-format-3:

Request Format:
^^^^^^^^^^^^^^^

``GET /l2vpn/1.0/ HTTP/1.1`` - Retrieve all active L2VPNs, meaning
L2VPN with **archived_date** has value 0.

``GET /l2vpn/1.0/archived HTTP/1.1`` - Retrieve all archived L2VPNs,
meaning L2VPN with **archived_date** value different than 0.

No request body is needed. This specification assumes that any request
body provided must be ignored by the SDX Controller.

.. _return-codes-3:

Return Codes:
^^^^^^^^^^^^^

200: OK

Return Body:

The return body must be a dictionary. If there are no L2VPNs, the
dictionary will be empty. If there are L2VPNs, a dictionary of
dictionaries must be used, where the key to each L2VPN will be its
**service_id**. Some examples:

-  No L2VPNs exist

   Request: GET /l2vpn/1.0/

   Return code: 200

   Return body: {}

-  One or More L2VPNs exist:

   Request: GET /l2vpn/1.0/

   Return code: 200

   Return Body:

   {

   “c73da8e1-5d03-4620-a1db-7cdf23e8978c”: {

   ::

        "service\_id": "c73da8e1-5d03-4620-a1db-7cdf23e8978c",

   “name”: “VLAN between AMPATH/300 and TENET/150”,

   “endpoints”: [

   {“port_id”: “urn:sdx:port:tenet.ac.za:Tenet03:50”, “vlan”: “150”},

   {“port_id”: “urn:sdx:port:ampath.net:Ampath3:50”, “vlan”: “300”}

   ],

   “description”: “Example 1”,

   “qos_metrics”: {

   “min_bw”: {

   “value”: 5,

   “strict”: false

   },

   “max_delay”: {

   “value”: 150,

   “strict”: true

   }

   },

   “notifications”: [

   {“email”: “user@domain.com”},

   {“email”: “user2@domain2.com”}

   ],

   “ownership”: “user1”,

   “creation_date”: “20240522T00:00:00Z”,

   “archived_date”: “0”,

   “status”: “up”,

   “state”: “enabled”,

   “counters_location”: “https://my.aw-sdx.net/l2vpn/7cdf23e8978c”,

   “last_modified”: “0”,

   “current_path”: [“urn:sdx:link:tenet.ac.za:LinkToAmpath”],

   ::

                  "oxp\_service\_ids": {"ampath.net": \["c73da8e1"\],

   | “Tenet.ac.za”: [“5d034620”]}
   | },
   | “fa2c99ca-30a9-4b51-8491-683c52e326a6”: {
   | “service_id”: “fa2c99ca-30a9-4b51-8491-683c52e326a6”,
   | “name”: “Example 2”,
   | “endpoints”: [
   | {“port_id”: “urn:sdx:port:tenet.ac.za:Tenet03:50”, “vlan”: “3500”},
   | {“port_id”: “urn:sdx:port:sax.br:router_01:50”, “vlan”: “3500”},
   | {“port_id”: “urn:sdx:port:ampath.net:Ampath3:50”, “vlan”: “3500”}
   | ],
   | “ownership”: “user2”,
   | “creation_date”: “20240422T00:00:00Z”,
   | “archived_date”: “0”,
   | “status”: “up”,
   | “state”: “disabled”,
   | “counters_location”: “https://my.aw-sdx.net/l2vpn/52e326a6”,
   | “last_modified”: “0”,
   | “current_path”: [“urn:sdx:link:tenet.ac.za:LinkToSAX”,
   | “urn:sdx:link:tenet.ac.za:LinkToAmpath”,
   | “urn:sdx:link:ampath.net:LinkToSAX”],
   | “oxp_service_ids”: {“ampath.net”: [“d82da7f9”],
   | “tenet.ac.za”: [“ab034673”],
   | “sax.br”: [“bb834633”]}
   | }
   | }

Deleting a SDX L2VPN
--------------------

.. _description-4:

Description
^^^^^^^^^^^

SDX users must be able to delete their own SDX L2VPNs. Authentication
and authorization are outside of the scope of this document. SDX users
must use the previously provided **service_id** when requesting a
service deletion.

.. _sdx-internal-operation-3:

SDX Internal Operation
''''''''''''''''''''''

When deleting a SDX service, the SDX Controller must update the
following L2VPN attributes:

-  **archived_date**: this field must be updated with the datetime of
   the request.
-  **status**: “down”
-  **state**: “disabled”
-  **last_modified**: this field must be updated with the datetime of
   the request.

SDX L2VPNs must be stored in persistent storage for accountability
purposes. Deleting SDX L2VPNs can not be undone.

The SDX Controller must delete the L2VPNs immediately after receiving
the user request.

If a VLAN range was requested in the original SDX L2VPN service,
deleting that SDX L2VPN should be propagated to all OXP L2VPNs.

**Scheduling**: Since SDX L2VPNs have the option of scheduling service
decommissioning (**end_time** attribute), when the time comes, the SDX
Controller must delete the L2VPN following the same methodology
described in this section.

.. _request-format-4:

Request Format
^^^^^^^^^^^^^^

DELETE /l2vpn/1.0/{service_id} HTTP/1.1

.. _return-codes-4:

Return Codes
^^^^^^^^^^^^

| 201: L2VPN Deleted
| 401: Not Authorized
| 404: L2VPN Service ID provided does not exist.

Return Body:

None

.. [1]
   REST:
   https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm

.. [2]
   OpenAPI: https://www.openapis.org/

.. [3]
   Make sure to distinguish network interface from application interface
   or API: network interface is the physical or logical port on a
   network device where users or network services are terminated (or
   transported through). The use of “network interface” instead of
   network port is widespread to avoid confusion with the “port” concept
   in the Transport Layer (TCP, UDP, etc).

.. [4]
   In this document, the concept of dictionary, data dictionary, and
   Python dictionary have the same meaning. For more information, visit
   https://www.w3schools.com/python/python_dictionaries.asp

.. [5]
   Method for Estimation of Residual Bandwidth:
   https://patents.google.com/patent/US20110228695A1/en

.. [6]
   JSON: https://www.json.org/json-en.html

.. [7]
   https://docs.python.org/3/library/enum.html
