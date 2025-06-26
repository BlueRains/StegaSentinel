"""This module represents all models.

Function get_model will return a subclass instance of `PredictingModel`.
If no appropiate subclass depending on the mime type is found,
it will raise a `NoModelError`.

"""

__all__ = ["NoModelError", "PredictingModel", "get_model"]

from .errors import NoModelError
from .model import PredictingModel
from .sample_set import SamplePairModel

models = {"image/png": SamplePairModel()}


def get_model(mime_type: str) -> PredictingModel:
    """
    Based on the mime extension given, return the appropriate prediction model.

    Args:
        mime_type (str): The mime type to determine the model.

    Returns:
        PredictingModel: An prediction model.
    """
    if mime_type in models:
        return models[mime_type]
    raise NoModelError(mime_type)
