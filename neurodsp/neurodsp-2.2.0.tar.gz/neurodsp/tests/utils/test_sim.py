"""Tests for neurodsp.utils.sim."""

from neurodsp.utils.sim import *

###################################################################################################
###################################################################################################

def test_set_random_seed():

    set_random_seed()
    set_random_seed(100)
