#!/usr/bin/python3
"""
Unitesting State
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class test_state(unittest.TestCase):
    """tests for state"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.st = State()
        self.st.name = "HI"
        self.st.state_id = "CA"

    def test_self(self):
        """test attributes of State"""
        self.assertTrue(hasattr(State, "__str__"))
        self.assertTrue(hasattr(State, "save"))
        self.assertTrue(hasattr(State, "to_dict"))
        self.assertTrue(hasattr(State, "name"))

    def test_string(self):
        """test if State is a string"""
        ok = State()
        self.assertEqual(type(ok.name), str)
        self.assertEqual(type(ok.id), str)

    def test_creat_update(self):
        """test created at and updated at as well"""
        ok = State()
        self.assertEqual(datetime, type(ok.created_at))
        self.assertEqual(datetime, type(ok.created_at))

    def test_save(self):
        """testing save method"""
        self.st.save()
        self.assertNotEqual(self.st.created_at, self.st.updated_at)

    @classmethod
    def tearDownClass(self):
        """Tearing it all down by deletion"""
        del self.st

if __name__ == "__main__":
    unittest.main()
