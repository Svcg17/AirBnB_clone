#!/usr/bin/python3
"""Unitest user"""
import unittest
from models.user import User
from models.base_model import BaseModel


class test_user(unittest.TestCase):
    """Unitest user"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.foo = User()

    def test_inst(self):
        """some tests for instance"""
        self.assertIsInstance(self.foo, User)
        self.assertIsInstance(self.foo.email, str)
        self.assertIsInstance(self.foo.password, str)
        self.assertIsInstance(self.foo.first_name, str)
        self.assertIsInstance(self.foo.last_name, str)

    def test_to_dict(self):
        """testing to_dict method"""
        self.assertEqual('to_dict' in dir(self.foo), True)

    def test_subclass(self):
        """testing if subclass"""
        self.assertTrue(issubclass(self.foo.__class__, BaseModel), True)

    def test_is_subclass(self):
        """Tests to see if User is a subclass of BaseModel"""
        ok = User()
        self.assertEqual(issubclass(type(ok), BaseModel), True)

    def test_id(self):
        """ test for valid id"""
        ok = User()
        self.assertEqual(str, type(ok.id))

    @classmethod
    def tearDown(self):
        """tearing it down by deleting self.foo"""
        del self.foo

if __name__ == "__main__":
    unittest.main()
