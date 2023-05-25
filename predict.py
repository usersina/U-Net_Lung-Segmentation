import numpy as np
from PIL import Image


def mask_to_image(mask):
    return Image.fromarray((mask * 255)).astype(np.uint8)
