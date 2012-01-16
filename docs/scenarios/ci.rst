Continuous Integration
======================


Why?
----

Martin Fowler, who first wrote about `Continuous Integration <http://martinfowler.com/articles/continuousIntegration.html>`_ (short: CI) together with Kent Beck, describes the CI as follows:

    Continuous Integration is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily - leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop cohesive software more rapidly.

Jenkins
-------

`Jenkins CI <http://jenkins-ci.org>`_ is an extensible continuous integration engine. Use it.



Buildbot
--------
`Buildbot <http://buildbot.net/buildbot/docs/current>`_ is a Python system to automate the compile/test cycle to validate code changes. 


Mule?
-----

.. todo:: Write about Mule

Tox
---

`tox <https://bitbucket.org/hpk42/tox>`_ is an automation tool providing packaging, testing and deployment of Python software right from the console or CI server.
It is a generic virtualenv management and test command line tool which provides the following features:

* Checking that packages install correctly with different Python versions and interpreters
* Running tests in each of the environments, configuring your test tool of choice
* Acting as a frontend to Continuous Integration servers, reducing boilerplate and merging CI and shell-based testing.