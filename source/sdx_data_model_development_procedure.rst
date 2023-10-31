SDX Data Model Development
==========================

The AW-SDX data model is used in multiple components of the distributed
software system, some of which, the OXP provisioning system, are
supposed to be collaboratively supported by multiple development teams.
Along with the system and services, the data model specification will
also evolve that should be followed by updates in schemas,
implementations, and validations. This document describes the standard
procedure for this process to ensure the consistency of data model among
all the components.

The overall update workflow is shown in the figure with more detailed
tasks followed.

Step 1: Update the data model specification document with a new version number.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(https://drive.google.com/drive/folders/1_IsB9O9x1dF5zvBI-txRyR6aVuck4vZ_)

Step 2: Update the “datamodel” repo to conform to the latest version of above specification.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(https://github.com/atlanticwave-sdx/datamodel)

2.1 update JSON Schema

2.2 update the parser and validation software

2.3 update and pass all the unit tests

Step 3: Update the ‘sdx-lc’ repo to conform to the latest datamodel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(https://github.com/atlanticwave-sdx/sdx-lc)

3.1 Update the schema definition in the OpenAPI swagger.yaml

3.2 Test and validate the sdx-lc with the updated schema.

Step 4: Update the ‘sdx-controller’ repo to conform to the latest datamodel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(https://github.com/atlanticwave-sdx/sdx-controller)

4.1 Update the schema definition in the OpenAPI swagger.yaml

4.2 Test and validate the sdx-controller with the updated schema.
