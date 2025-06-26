"""This module implements Sample Set analysis.

Translated from Java of https://github.com/Ocram95/Modified-StegExpose/blob/main/SamplePairs.java

"""

from operator import add

import numpy as np
from PIL import Image

from .model import PredictingModel


def pair_type(pixel1, pixel2):
    """Determine which categories a pair falls in.

    1. Identical pixels
    2. Identical but for their lsb
    3. pixel1 lower than pixel2, and lsb pixel2 is 0
    3.1. pixel1 higher than pixel2, and lsb pixel2 is 1
    4. Opposite of 3
    Returns as a list of points
    """
    res = [0, 0, 0, 0]
    if (pixel1 ^ pixel2) >> 1 == 1:
        # If pixel 1 is identical to pixel 2, except the lsb differs
        res[0] += 1
    lsb_2 = pixel2 & 1
    if pixel1 == pixel2:
        # If identical
        res[1] += 1
    elif (not lsb_2 and pixel1 < pixel2) or (lsb_2 and pixel1 > pixel2):
        res[2] += 1
    else:
        res[3] += 1
    return res


class SamplePairModel(PredictingModel):
    """Use the sample pair analysis to determine if an attachment is a stego object."""

    threshold = 0.2

    def channel_analysis(self, channel: Image.Image) -> float:
        """Calculate the sample-pair number for a single channel in the image."""
        w, h = channel.size
        pairs = [0, 0, 0, 0]
        pair_count = 0
        # Pairs horizontally
        for y in range(h):
            for x in range(0, w, 2):
                pixel1, pixel2 = channel.getpixel((x, y)), channel.getpixel((x + 1, y))
                pairs = map(add, pairs, pair_type(pixel1, pixel2))
                pair_count += 1
        # Pairs vertically
        for x in range(0, w):
            for y in range(0, h, 2):
                pixel1, pixel2 = channel.getpixel((x, y)), channel.getpixel((x, y + 1))
                pairs = map(add, pairs, pair_type(pixel1, pixel2))
                pair_count += 1

        # Return the smallest of the roots
        lsb_mismatch, Z, X, identical = pairs  # noqa:N806
        a = 0.5 * (lsb_mismatch + Z)
        b = 2 * X - pair_count
        c = identical - X
        roots = np.roots([a, b, c])
        return min(roots)

    def image_analysis(self, image: Image.Image) -> float:
        """Sample analysis of the entire image.

        Args:
            image (Image.Image): The image
        """
        band_count = len(image.getbands())
        total_number = 0
        for option in image.getbands():
            total_number += self.channel_analysis(image.getchannel(option))
        val = total_number / band_count
        return min(abs(val), 1)

    def is_stego_object(self, attachment: bytes) -> bool:  # noqa: D102
        with Image.open(attachment) as image:
            return self.image_analysis(image) > self.threshold
