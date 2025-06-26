"""This package contains the code for the analyser module.

It provides functionality to analyze email attachments in a secure environment
using Docker containers. The analysis is performed based on the file type of the
attachment, and results are returned indicating whether the attachment is safe or not.

`analyse_attachment` is run for each attachment that comes in.

The result is sent back as a `Result`.
"""
