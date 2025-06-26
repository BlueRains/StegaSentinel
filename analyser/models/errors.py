"""Document errors that can happen by models."""


class NoModelError(Exception):
    """Raised when there is no model to check that image type."""

    def __init__(self, mime):
        message = f"No model for file type {mime} found."
        super().__init__(message)
