"""The main entry point for the connector.

It will fetch new emails, extract attachments,
and analyse them in a secure docker container with a model depending on the file type.
"""

import json
import logging
import os
import socket

from attrs import define, field
from emails import Attachment, EmailHandler, EmailId

logger = logging.getLogger(__name__)


@define
class Result:
    """The result of testing."""

    filetype: str
    """The detected filetype of the attachment"""
    checked: bool = field(default=False)
    """Whether it was able to check if it was safe"""
    safe: bool = field(default=False)
    """Whether steganography was detected"""


def handle_attachment(attachment: Attachment) -> bool:
    """Handle an email attachment by analyzing it in a secure environment.

    This function runs a isolated Docker container to analyze the attachment.
    It uses one of the available models based on the file type of the attachment.
    If it is unable to analyse the attachment, it will log a warning and identify
    it as safe.

    Args:
        attachment (Attachment): The attachment to analyse.

    Returns:
        bool: True if it's safe, False if it should be quarantined.
    """
    logger.info(f"Analyzing attachment: {attachment.filename}")
    client = socket.create_connection(
        (os.environ["NETWORK"], int(os.environ["COMM_PORT"]))
    )
    client.send(attachment.content.read())
    raw_res = client.recv(1028)
    logger.debug("Recieved %d as result", raw_res)
    res = Result(**json.load(raw_res))
    if not res.checked:
        logger.warning("Unable to analyse attachment with filetype %d", res.filetype)
        return True
    if res.safe:
        logger.info("Attachment '%d' considered safe.", attachment.filename)
    return res.safe


def handle_email(handler: EmailHandler, id: EmailId):
    """Handle a specific email."""
    logger.debug("Handling email with ID: %s", id)
    attachments = handler.get_attachments(id)
    for attachment in attachments:
        if not handle_attachment(attachment):
            logger.error(
                "Quarantining email with ID %s due to unsafe attachment %s",
                id,
                attachment.filename,
            )
            handler.quarantine_email(id)
    handler.accept_email(id)
    logger.info("Email with ID %s considered safe.", id)


def main():
    """Handle everything."""
    handler: EmailHandler = EmailHandler()
    while True:
        if handler.new_emails_arrived():
            logger.info("New emails arrived.")
            new_emails = handler.get_new_emails()
            for email in new_emails:
                handle_email(handler, email)
