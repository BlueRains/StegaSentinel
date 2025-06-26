"""This module initializes the email handling package."""

from .email import Attachment, EmailHandler, EmailId
from .imap import ImapEmail

# Make sure to have custom created emails in
__all__ = ["Attachment", "EmailHandler", "EmailId", "ImapEmail"]
