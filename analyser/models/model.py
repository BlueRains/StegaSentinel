"""Defines a protocol for models that can predict steganography in attachments."""

from typing import Protocol


class PredictingModel(Protocol):
    """A protocol for models that can predict whether an attachment contains steganography.

    It must implement the `is_steganography` method which takes an attachment in bytes.
    """  # noqa: E501

    def is_stego_object(self, attachment: bytes) -> bool:  # noqa: ARG002
        """Check if an attachment contains steganography."""
        assert NotImplementedError("This method should be implemented by subclasses")
