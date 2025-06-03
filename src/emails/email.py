"""Define Attachment and abstract EmailHandler classes.

This defines the functions an email handler should implement.
Different implementations should inherit from this class.
Additionally, it defines an Attachment class to represent email attachments.
"""

from typing import Protocol

from attrs import define, field

UNIMPLEMENTED_SUBCLASS = "This method should be implemented by subclasses"


@define
class Attachment:
    """Class representing an email attachment.

    Args:
        filename: The name of the attachment file.
        content: The content of the attachment as bytes.
    """

    filename: str = field()
    content: bytes = field()


class EmailHandler(Protocol):
    """Abstract class for email handling.

    Should be able to detect and return any new emails that came in,
    and get any email attachments.
    """

    def new_emails_arrived(self) -> bool:
        """Check if new emails have arrived.

        Returns:
            True if new emails have arrived, False otherwise.
        """
        raise NotImplementedError(UNIMPLEMENTED_SUBCLASS)

    def get_new_emails(self):
        """Get new emails from the email server.

        Returns:
            A list of email ids that are new.
        """
        raise NotImplementedError(UNIMPLEMENTED_SUBCLASS)

    def get_attachments(self, email_id) -> list[Attachment]:
        """Get attachments from an email.

        Args:
            email_id: The ID of the email to get attachments from.

        Returns:
            A list of bytes representing the attachments.
        """
        raise NotImplementedError(UNIMPLEMENTED_SUBCLASS)

    def quarantine_email(self, email_id):
        """
        Quarantine an email by its ID.

        Args:
            email_id: The ID of the email to quarantine.
        """
        raise NotImplementedError(UNIMPLEMENTED_SUBCLASS)

    def accept_email(self, email_id):
        """
        Indicate that an email is safe and can be accepted.

        Args:
            email_id: The ID of the email to accept.
        """
        raise NotImplementedError(UNIMPLEMENTED_SUBCLASS)
