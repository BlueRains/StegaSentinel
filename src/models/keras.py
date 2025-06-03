"""Keras model for detecting steganography in attachments.

Should be used with a Keras model that has been trained for binary classification.
Needs a Keras model file path to initialize.
"""

from .model import PredictingModel


class KerasModel(PredictingModel):
    """A Keras model for detecting steganography in attachments."""
