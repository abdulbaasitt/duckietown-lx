from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[:, shape[1]//2:] = 1  # Positive weights to the right half of the image
    res[:, :shape[1]//2] = -1  # Negative weights to the left half of the image

    # these are random values
    # res[100:150, 100:150] = 1
    # res[300:, 200:] = 1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[:, :shape[1]//2] = 1  # Positive weights to the left half of the image
    res[:, shape[1]//2:] = -1  # Negative weights to the right half of the image
    # res[100:150, 100:300] = -1
    # ---
    return res
