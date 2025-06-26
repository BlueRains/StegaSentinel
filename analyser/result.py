"""This file provides the `Result` class."""

from attrs import define, field


@define
class Result:
    """The result of testing."""

    filetype: str
    """The detected filetype of the attachment"""
    checked: bool = field(default=False)
    """Whether it was able to check if it was safe"""
    safe: bool = field(default=False)
    """Whether steganography was detected"""
