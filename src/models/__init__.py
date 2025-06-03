"""This module provides functionality to retrieve prediction models based on mime types.

It contains all the predefined models and a function to get the appropriate model.
"""
__all__ = ["PredictingModel", "get_model"]

from .model import PredictingModel


def get_model(mime_type: str) -> PredictingModel:
    """
    Based on the mime extension given, return the appropriate prediction model.

    Args:
        mime_type (str): The mime type to determine the model.

    Returns:
        PredictingModel: A model has the
    """
    pass
