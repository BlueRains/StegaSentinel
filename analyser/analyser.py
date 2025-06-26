"""Analyze attachments for malicious content."""

import json
import logging
import os
import socket

import magic
from attrs import asdict
from models import NoModelError, get_model
from result import Result

logger = logging.getLogger(__name__)


def analyse_attachment(attachment: bytes) -> Result:
    """Analyze an attachment from stdin.

    Writes the JSON of Result to stout.
    """
    # Store file in memory
    file_type = magic.from_buffer(attachment, mime=True)
    res = Result(filetype=file_type)
    try:
        model = get_model(file_type)
        res.checked = True
        res.safe = model.is_stego_object(attachment)
    except NoModelError:
        return res
    return res


def main():
    """Wait for attachments.

    Create a serversocket.
    Whenever a connection is created, recieve the attachment size.
    Then recieve the attachment itself and send to be analysed.
    The result is made a JSON string and sent back.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        serversocket.bind((os.environ["NETWORK"], int(os.environ["COMM_PORT"])))
        serversocket.listen()  # become a server socket
        while True:
            connection, address = serversocket.accept()
            # We use an arbitrarily large number here
            # Because images etc. can get quite large
            attachment = connection.recv(1 << 32)
            if len(attachment) == 1 << 32:
                # Assume that this only happens if the file was too large
                # (and not the exact right size)
                logger.error("File too large! Trying to analyse a part.")
            res = analyse_attachment()
            item = json.dumps(asdict(res))
            connection.send(item)
            connection.close()


if __name__ == "__main__":
    main()
