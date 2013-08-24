Continuous Integration
======================


Why?
----

Martin Fowler, who first wrote about `Continuous Integration <http://martinfowler.com/articles/continuousIntegration.html>`_
(short: CI) together with Kent Beck, describes the CI as follows:

    Continuous Integration is a software development practice where members of
    a team integrate their work frequently, usually each person integrates at
    least daily - leading to multiple integrations per day. Each integration is
    verified by an automated build (including test) to detect integration errors
    as quickly as possible. Many teams find that this approach leads to
    significantly reduced integration problems and allows a team to develop
    cohesive software more rapidly.

Jenkins
-------

`Jenkins CI <http://jenkins-ci.org>`_ is an extensible continuous integration
engine. Use it.



Buildbot
--------
`Buildbot <http://docs.buildbot.net/current/>`_ is a Python system to
automate the compile/test cycle to validate code changes.


Mule?
-----

.. todo:: Write about Mule

Tox
---

`tox <http://tox.readthedocs.org/en/latest/>`_ is an automation tool providing
packaging, testing and deployment of Python software right from the console or
CI server. It is a generic virtualenv management and test command line tool
which provides the following features:

* Checking that packages install correctly with different Python versions and
  interpreters
* Running tests in each of the environments, configuring your test tool of
  choice
* Acting as a frontend to Continuous Integration servers, reducing boilerplate
  and merging CI and shell-based testing.


Travis-CI
---------
`Travis-CI <http://travis-ci.org/>`_ is a distributed CI server which builds tests
for open source projects for free. It provides multiple workers to run Python tests
on and seamlessly integrates with Github. You can even have it comment on your Pull
Requests whether this particular changeset breaks the build or not. So if you are
hosting your code on Github, travis-ci is a great and easy way to get started with
Continuous Integration.

In order to get started, add a ``.travis.yml`` file to your repository with this
example content::

    language: python
    python:
      - "2.5"
      - "2.6"
      - "2.7"
      - "3.1"
      - "3.2"
    # command to install dependencies
    script: python tests/test_all_of_the_units.py
    branches:
      only:
        - master


This will get your project tested on all the listed Python versions by running the given
script and only build the master branch. There are a lot more options you can enable, like
notifications, before and after steps and much more. The
`travis-ci docs <http://about.travis-ci.org/docs/>`_ explain all of those and are very
thorough.

In order to activate testing for your project, go to `the travis-ci site <http://travis-ci.org/>`_
and login with your Github account. Then activate your project in your profile settings and that's
it. From now on, your project's tests will be run on every push to Github.
