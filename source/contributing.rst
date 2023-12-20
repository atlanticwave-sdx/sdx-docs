================================
Contributing to AtlanticWave-SDX
================================

Thank you for taking the time and effort to contribute to
AtlanticWave-SDX. We would love to have you join the project.

The below summarizes the processes that we try to follow. This
document is work in progress, somewhat aspirational rather than a
description of reality, and thus is subject to change based on
feedback.

In summary, you are expected to follow a lightweight process that is
known as `GitHub flow`_.  You will need to:

- Report issues when you find them, or create an issue when you intend
  to develop a new feature.

- Make code changes with GitHub `pull requests`_, ask for feedback on
  your changes, and address feedback.


Reporting issues
================

If you find a new issue, please consider reporting it.  Be sure to
include enough details for a developer to be able to reproduce the
issue. Be sure to check existing issues, open and closed, before
reporting an issue to see that if anyone else has already reported it.

Do you want to add a feature in AtlanticWave-SDX?  Please create an
issue for that too, and label it as an “enhancement”.  Describe the
feature that you would like to see in detail.  Discussing features
this way, *before* you spend a bunch of time working on it, is a good
way to sure that we are better prepared to review the work, give
feedback on it, and to avoid duplicate work.

If you would like to implement the feature, or fix an issue that you
have reported, you should use GitHub pull requests.


Submitting pull requests
========================

We try to follow a pull-request based workflow, as described in
`GitHub flow`_ document. A pull-request based workflow will ensure
that we are better coordinated. It will ensure that changes are better
understood by everyone, not just the person making the changes.

Pushing commits directly to ``main`` branch is discouraged. In order to
enforce a pull-request based workflow, we protect the ``main`` branches,
at least in a subset of our repositories.

When creating a pull request, below are the steps you should follow:


1. Create an issue
------------------

Create an issue, in the repository where you want to create a pull
request. Describe the feature you want to implement, or the issue you
want to fix. This will help your collaborators to know what you are up
to. Issues will be also a good place to discuss your idea, and collect
feedback.


2. Create a branch
------------------

Check out the source code of the repository, if you have not done so
already. And then create a branch for the pull request.

.. code:: console

   git fetch
   git checkout -b nn.issue-description-oneliner origin/main

A branch name scheme like ``nn.issue-description-oneliner`` (where
``nn`` stands for the issue number for the issue you just created, and
``issue-description-oneliner`` is a string that briefly describes the
purpose of the branch) is suggested, but not mandatory. This scheme
however makes it easy to find a branch in your local development setup
or from GitHub, when you have several branches in progress at a time.


3. Make your changes
--------------------

Make the changes that you want.

You will want to follow the guidelines documented in the relevant
repository. Make sure that the tests pass. If you are adding a
nontrivial amount of new code, make sure that your code has adequate
test coverage.


4. Test your changes
--------------------

You should test your changes manually.  You should also write some
unit and integration tests to automate testing of your changes.

We use `pytest`_ framework to write the tests, and `tox`_ to run the
tests in an isolated environment.  Look for existing examples in the
repository you are working on.  In most cases, you can run the tests
by setting some environment variables when necessary, and running
``tox``.

You are also expected to format your code using `black`_ and `isort`_.
It would be a good idea to check your code using a linter such as
`ruff`_ or `flake8`_.

We distinguish between two types of code that need to be tested in
different ways before PR.

1. Function test: The developer is responsible to provide the basic
   test cases for every major class and function, such as those in the
   PCE and DataModel repos, with an example input either through
   providing a main function or unittest.

2. Component test: integration/interaction with other components, like
   SDX-LC to OXP and SDX-LC to SDX-Controller, or the RabbitMQ Message
   Queue subsystem with SDX-LC and SDX-controller.

   1. Unittest: Device the input and the expected output data models
      in JSON: (1) Mock topology in JSON; (2) mock request in JSON.

   2. RestAPI test: Swagger mock test for both end points and data
      model validation

   3. VM Testbed test: Deploy your own AW-SDX in the testbed and test
      the endpoints with the mock input data models


5. Push the branch
------------------   

If you do not have commit access to the repository, you may need to
fork the repository, and push the branch there. If you do have commit
access to the repository, you may be able to push your branch there.

.. code:: console

   git push origin nn.issue-description-oneliner


6. Create a pull request
------------------------

You might want to refer GitHub's documentation about `creating`_ pull
requests.

AtlanticWave-SDX repositories are set up to run some checks against
pull requests when you create them or update them.  The checks
include:

- Unit and integration tests,
- Packaging checks to ensure that there are no broken dependencies,
- Code coverage checks to ensure that new code has test coverage,
- Code formatting checks, and  
- Linters and other possible checks.

Pull requests cannot be merged to ``main`` branch if they do not pass
these checks.  One or more approving reviews are also required before
a pull request can be merged.


7. Wait for feedback
--------------------

If your collaborators have feedback for you, they will leave the
feedback on your pull request. Or they may simply approve your pull
request.


8. Address feedback
-------------------

If there is feedback on the pull request, you may want to address the
feedback by making further changes.


9. Wait for the pull request to be merged
-----------------------------------------

At this stage, one of these things should happen:

- A collaborator with merge rights will approve and merge your pull
  request.

- If a collaborator has approved your pull request, and if you have
  the rights to merge the pull request, you should merge it yourself.


General notes
=============


3. How to work with each other
==============================

Each main component has its lead developer. It is important to follow
a simple workflow between different modules in order to avoid
duplicated work and inefficiency caused by confusion.

1. When review and integrate with other modules, please first review
   and test with their specifications, APIs and main functions.

2. If you think something is missing or not correct in another’s
   module, please first write a **feature request** to be reviewed by
   that module’s developer.

3. After an agreement is reached, the module’s developer is
   responsible to design the new feature and get the approval with the
   requester.

4. The module’s developer is responsible to implement and test the new
   feature.

5. Then integration test will be conducted and PR procedure will be
   followed to accept the new implementation.


Code Style (PEP8)
=================

.. todo:: write this.


Closing Remarks
===============

AtlanticWave-SDX is based on a service-oriented architecture
consisting of multiple containerizable components.  While being
distributed and deployable independently, these components are
developed with REST API endpoints and message queues, with data models
and messages following carefully designed specifications so that they
communicate with each other to accomplish the end-to-end provisioning
and other control workflows.

AtlanticWave-SDX software team consists of a few developers and does
not have a separate QA team.  Therefore it is important for each
developer to follow certain high-level rules and conventions that are
laid out above.


.. _`GitHub flow`: https://docs.github.com/en/get-started/quickstart/github-flow
.. _`pull requests`: https://docs.github.com/en/pull-requests
.. _`creating`: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

.. _`pytest`: https://pypi.org/project/pytest/
.. _`tox`: https://pypi.org/project/tox/
.. _`black`: https://pypi.org/project/black/
.. _`isort`: https://pypi.org/project/isort/
.. _`ruff`: https://pypi.org/project/ruff/
.. _`flake8`: https://pypi.org/project/flake8/
