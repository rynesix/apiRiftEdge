# test_apirift.py
"""
Tests for apiRift module.
"""

import unittest
from apirift import apiRift

class TestapiRift(unittest.TestCase):
    """Test cases for apiRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = apiRift()
        self.assertIsInstance(instance, apiRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = apiRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
