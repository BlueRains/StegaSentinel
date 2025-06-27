Usage
=====

.. _installation:

Installation
------------

To use StegaSentinel, Docker must be installed.

Additionally, a '.env' file must be created.
This file needs to have at least the following variables:

.. envvar:: NETWORK
   
   The network for the docker containers to communicate with. Default: localhost

.. envvar:: COMM_PORT

   The port for the docker containers to communicate with.



.. code-block:: console

   (.venv) $ docker compose up

It will automaticall start up both the connector and the analyser in different docker containers.


Email
-------
For different email integrations, different libraries etc. can be needed.

IMAP
++++++
For IMAP, the following environment variables are needed:

.. envvar:: IMAP_HOST

   The IMAP server.

.. envvar:: IMAP_PORT

   The port of the IMAP server

.. envvar:: IMAP_USER

   The email / username of the user.

.. envvar:: IMAP_PASS

   The password needed to connect.