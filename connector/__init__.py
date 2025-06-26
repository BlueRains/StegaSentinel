"""This package contains the code for the connection module.

It provides the connection between the email and the isolated sandbox.
Whenever an email comes in, it sends it to the sandbox and reads the result.
Based on that, it isolates the email, warn the user about it or send it to the inbox.

`main.py` is run on startup.
"""
