#!/usr/bin/python3
"""
Unitesting State
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class test_state(unittest.TestCase):
    """tests for state"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.st = State()
        self.st.name = "HI"
        self.st.state_id = "CA"

    def test_attr(self):
        """test attributes of State"""
        self.assertTrue('name' in self.st.state_id.__dict__)
        self.assertTrue('id' in self.st.__dict__)
        self.assertTrue('created_at' in self.st.__dict__)
        self.assertTrue('updated_at' in self.st.__dict__)

    def test_string(self):
        """test if State is a string"""
        self.assertEqual(type(self.st.name), str)
        self.assertEqual(type(self.st.state_id), str)

    def test_save(self):
        """testing save method"""
        self.st.save()
        self.assertThat(self.st.created_at, not (self.st.updated_at))

    @classmethod
    def tearDownClass(self):
        """Tearing it all down by deletion"""
        del self.st

if __name__ == "__main__":
    unittest.main()
