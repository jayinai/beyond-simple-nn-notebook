"""
  Some utilities.
"""

import numpy as np


def preprocess(img_matrix):
  return np.expand_dims(img_matrix, axis=-1).astype('float32') / 255