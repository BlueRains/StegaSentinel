"""This module demonstrates a connection to a IMAP server."""

import contextlib
import logging
import os
from email import message_from_bytes, policy
from email.message import EmailMessage
from imaplib import IMAP4
from io import BytesIO

from dotenv import load_dotenv

from .email import Attachment, EmailHandler
from .errors import CommandFailedError, NoConnectionError

load_dotenv()
logger = logging.getLogger(__name__)


@contextlib.contextmanager
def connection():
    """Create a connection to the IMAP server."""
    try:
        inbox = IMAP4(os.environ.get("IMAP_HOST"), os.environ.get("IMAP_PORT"))
        res, _ = inbox.login(os.environ.get("IMAP_USER"), os.environ.get("IMAP_PASS"))
        if res != "OK":
            raise NoConnectionError(os.environ.get("IMAP_HOST"))
        yield inbox
    finally:
        inbox.close()
        inbox.logout()


class ImapEmail(EmailHandler):
    """Implements EmailInterface for IMAP email handling."""

    def __init__(self):
        self.host = os.environ.get("IMAP_HOST")

    def new_emails_arrived(self) -> bool:  # noqa: D102
        with connection() as inbox:
            inbox.select("inbox")
            # Server can only send a reply if you send a command
            # Therefore a noop to check if recent messages arrived.
            status, messages = inbox.noop()
            if status != "OK":
                # The connection
                raise NoConnectionError(self.host)
            return bool(messages[0])
        raise NoConnectionError(self.host)

    def get_new_emails(self):  # noqa: D102
        with connection() as inbox:
            typ, res = inbox.search(None, "UNSEEN")
        pass

    def get_attachments(self, email_id: str):  # noqa: D102
        with connection() as inbox:
            status, data = inbox.fetch(email_id, "(RFC822)")
            if status != "OK":
                raise CommandFailedError(f"FETCH {email_id}", status)
            msg: EmailMessage = message_from_bytes(data[0][1], policy=policy.default)
            for part in msg.iter_attachments():
                name = part.get_filename()
                content = part.get_content()
                # Make sure the content is in bytes
                if isinstance(content, bytes):
                    yield Attachment(name, BytesIO(content))
                else:
                    yield Attachment(name, BytesIO(content.encode()))

    def accept_email(self, email_id):  # noqa: D102
        logger.info("Email %d accepted", email_id)

    def quarantine_email(self, email_id: str):  # noqa:D102
        with connection() as inbox:
            inbox.store(email_id, "+FLAGS", "\\Junk")
        logger.info("Email %d quarantined (set Junk flag)", email_id)
