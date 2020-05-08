.. _publishing-your-code-ref:


####################
Publishing Your Code
####################

.. todo:: Replace this kitten with the photo we want.

.. image:: https://placekitten.com/800/600

A healthy open source project needs a place to publish its code and project
management stuff so other developers can collaborate with you. This lets your
users gain a better understanding of your code, keep up with new developments,
report bugs, and contribute code.

This development web site should include the source code history itself, a bug
tracker, a patch submission (aka "Pull Request") queue, and possibly additional
developer-oriented documentation.

There are several free open source project hosting sites (aka "forges"). These
include GitHub, SourceForge, Bitbucket, and GitLab. GitHub is currently the best.
Use GitHub.


*********************************
Creating a Project Repo on GitHub
*********************************

To publish your Python project on GitHub:

1. Create a GitHub account if you don't already have one.

2. Create a new repo for your project.

   1. Click on the "+" menu next to your avatar in the upper right of the page and choose "New repository".

   2. Name it after your project and give it an SEO-friendly description.

   3. If you don't have an existing project repo, choose the settings to add a
      README, `.gitignore`, and license. Use the Python `.gitignore` option.

3. On the newly created repo page, click "Manage topics" and add the tags "python" and "python3" and/or "python2" as appropriate.

4. Include a link to your new GitHub repo in your project's README file so people who just have the project distribution know where to find it.

If this is a brand new repo, clone it to your local machine and start working:

.. code-block:: console

    $ git clone https://github.com/<username>/<projectname>

Or, if you already have a project Git repo, add your new GitHub repo as a remote:

.. code-block:: console

    $ cd <projectname>
    $ git remote add origin https://github.com/<username>/<projectname>
    $ git push --tags

***********************
When Your Project Grows
***********************

For more information about managing an open source software project, see the book
`Producing Open Source Software <https://producingoss.com/>`_.
