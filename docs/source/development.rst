Development
=====

Installation
------------
First, follow the :ref:`installation instructions <installation>`

Install pipenv. Optionally, install pyenv.

.. code-block::
   pip install pipenv

Install the development packages using

.. code-block::
   pipenv install --dev

If you will be working on the connector package or the analyser package, 
run the following command, replacing "package" with the correct name.

.. code-block::
   pipenv install --categories="package"

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