import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

FILENAME = "problem2.py"

def test_translate_particles():
    value = get_attribute("result2e", FILENAME)
    assert_almost_equal(value,
                        np.array([[ 1.34234, -1.34234, -1.34234],
                                  [ 2.68468,  0.     , -1.34234],
                                  [ 2.68468, -1.34234,  0.     ],
                                  [ 1.34234,  0.     ,  0.     ]]))

