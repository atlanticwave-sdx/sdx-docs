AtlanticWave-SDX 2.0 Release Notes 
==================================

Overview
--------

The AtlanticWave-SDX 2.0 project achieves its goals by providing a
standardized interface (SDX-LC) between the SDX Controller and different
OXPOs. This abstraction layer enables the SDX Controller to communicate
with various OXPOs using a consistent data model, regardless of the API
variations in other solutions.

Components
----------

- Open eXchange Points (OXPs): Open eXchange Points (OXPs) facilitate
  data exchange between networks.

- Each OXP consists of two essential elements:

  - Network Orchestrator (OXPO): Automated network configuration,
    flow, and traffic engineering policies.

  - SDX Local Controller (SDX-LC): Acts as a bridge between the OXPO
    and the centralized SDX Controller.

OXPO Selection
--------------

- Each OXP's network operation team independently defines and manages
  its OXPO.

- Different OXPOs are integrated into the AtlanticWave-SDX ecosystem.

- AmLight Open Exchange Point (OXP) leverages the Kytos-ng
  Software-Defined Networking (SDN) platform.

- SAX OXP deploys OESS 2.0 for network orchestration, not included in
  this release.

Inter-Domain Provisioning
-------------------------

- OXPs open their interfaces to accept provisioning requests and
  export topology updates.

- SDX-LC uses each OXPO's API to retrieve topological information and
  push provisioning requests.

SDX-LC Functionality
--------------------

The SDX-LC module facilitates the translation of instructions from the
data model of the centralized SDX Controller to the API of each OXPO. It
simplifies the communication process and ensures compatibility with
existing APIs.

OXPO API Variations
-------------------

- Different OXPOs may have variations in their interfaces.

- Kytos-ng provide APIs for exporting topological data and receiving
  service provisioning requests.

System Design
-------------

- The system design integrates Kytos-ng OXPOs with SDX-LC.

- Three approaches are considered for gathering topology data
  depending on OXPO support for the AW-SDX 2.0 Topology Data Model
  specification. First approach is part of this release:

- The OXPO supports the AW-SDX 2.0 Topology Data Model specification
  and pushes the topology data to the SDX-LC OpenAPI interface

Additional Elements in SDX Topology
-----------------------------------

The SDX topology includes elements such as Name, Id, Timestamp, and
Version control for better management and versioning.

MEICAN Integration
------------------

- MEICAN web application offers support to create circuits.

- It retrieves and maps topology information from the SDX-Controller
  endpoint.

- ORCID/CI Login Authentication is introduced for users.

- The framework supports adding user permissions based on roles.

API Testing
-----------

- API testing ensures functional accuracy, security, performance,
  contract compliance, and system reliability.

- Various types of tests, including unit tests, functional tests,
  integration tests, and end-to-end tests, are conducted to validate
  the system's behavior and functionality.

GitHub Setup
-------------

- The GitHub repository "sdx-continuous-development" contains
  submodules for integrating components like Kytos-ng, OXPOs, SDX-LC,
  SDX Controller, and Meican.

- The environment setup script configures the host machine with
  necessary tools.

Building the Environment
------------------------

Commands are provided to build the Kytos-ng components, OXPOs, and
MongoDB container.

Applying Patches
----------------

The repository may require patches for specific configurations or bug
fixes.

Running the Integration
-----------------------

- Docker Compose is used to orchestrate the system, running containers
  for Kytos-ng, SDX-LC, MongoDB, Mininet, and RabbitMQ.

- These release notes provide an overview of the AtlanticWave-SDX 2.0
  project, its components, system design, and testing procedures.
  They highlight the integration of various OXPOs, Meican, and the
  importance of API testing for system reliability and
  functionality. The GitHub setup and environment building steps are
  also detailed.
          
