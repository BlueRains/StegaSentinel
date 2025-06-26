"""Documents errors for email handling."""


class NoConnectionError(Exception):
    """Raised when there is no connection to an email server."""

    def __init__(self, server):
        message = f"No connection could be made to the {server} server."
        super().__init__(message)


class CommandFailedError(Exception):
    """Raised when a command sent to the email server fails."""

    def __init__(self, command: str, response: str):
        message = f"Command '{command}' failed with response: {response}"
        super().__init__(message)
