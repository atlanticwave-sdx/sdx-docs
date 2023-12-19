================================
Contributing to AtlanticWave-SDX
================================

Thank you for taking the time and effort to contribute to
AtlanticWave-SDX. We would love to have you join the community.

The below summarizes the processes that we try to follow. This
document is work in progress, somewhat aspirational rather than a
description of reality, and thus is subject to change based on
feedback.


Reporting Issues
================

Please check the existing issues, open and closed, before reporting an
issue to see that if anyone else has reported your issue already.

If you find a new issue, please consider reporting it. Be sure to
include enough details for us to be able to reproduce your issue.

Do you want to implement a feature in AtlanticWave-SDX? Please create an
issue for that too, and label it as an “enhancement”. Describe the
feature that you would like to see in detail. Discussing features this
way, *before* you spend a bunch of time working on it, is a good way to
sure that we are better prepared to review the work, give feedback on
it, and to avoid duplicate work.

If you would like to implement the feature, or fix an issue that you
have reported, you should use GitHub pull requests.


Submitting Pull Requests
========================

We try to follow a pull-request based workflow, as described in
“`GitHub <https://docs.github.com/en/get-started/quickstart/github-flow>`__”
document. A pull-request based workflow will ensure that we are better
coordinated. It will ensure that changes are better understood by
everyone, not just the person making the changes.

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


3. Make Your Changes
--------------------   

Make the changes that you want.

You will want to follow the guidelines documented in the relevant
repository. Make sure that the tests pass. If you are adding a
nontrivial amount of new code, make sure that your code has adequate
test coverage.


4. Push the branch
~~~~~~~~~~~~~~~~~~

If you do not have commit access to the repository, you may need to
fork the repository, and push the branch there. If you do have commit
access to the repository, you may be able to push your branch there.

.. code:: console

   git push origin nn.issue-description-oneliner


5. Create a Pull Request
------------------------   

See `GitHub’s docs
<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`__
about Pull Requests.

We are in the process of setting up continuous integration on our main
repositories. We are likely to enforce the policy that (1) tests will
run against pull requests, and (2) pull requests must pass tests
before they are merged.


6. Wait for Feedback
--------------------   

If your collaborators have feedback for you, they will leave the
feedback on your pull request. Or they may simply approve your pull
request.


7. Address Feedback
-------------------   

If there is feedback on the pull request, you may want to address the
feedback by making further changes.


8. Wait for the Pull Request to be Merged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this stage, one of these things should happen:

- A collaborator with merge rights will approve and merge your pull
  request.

- If a collaborator has approved your pull request, and if you have
  the rights to merge the pull request, you should merge it yourself.


[PREV] Contributing to AtlanticWave-SDX
=======================================


1. Writing Code
===============

1. Go through and get a clear understanding on functions, data models,
   and interfaces of different system components.

2. Propose the implementation design to be reviewed within the team.

3. Create a meta issue in identify the implementation goals, modules,
   and functions agreed upon by the team review.

4. Create a branch to develop the code.

5. Follow Section 2 and 3 for the continuous code development.


2. Testing Code before submitting a PR request
==============================================

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


Pull Request (PR) iteration with the established CI/CD workflow in Github
=========================================================================



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


