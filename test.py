"""tests for compute.py
"""

from leetcode import setup_driver

def test_setup_driver():
    assert(hasattr(setup_driver(), 'get'))
