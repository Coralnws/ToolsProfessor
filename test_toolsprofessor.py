# test_toolsprofessor.py
"""
Tests for ToolsProfessor module.
"""

import unittest
from toolsprofessor import ToolsProfessor

class TestToolsProfessor(unittest.TestCase):
    """Test cases for ToolsProfessor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ToolsProfessor()
        self.assertIsInstance(instance, ToolsProfessor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ToolsProfessor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
