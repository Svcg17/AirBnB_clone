#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
"""test for city"""


class test_city(unittest.TestCase):
    """tests for ciy"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.cityy = City()
        self.cityy.name = "SF"
        self.cityy.state_id = "OR"

    def test_city(self):
        """some tests for instance of city"""
        self.assertIsInstance(self.cityy, City)
        self.assertIsInstance(self.cityy.state_id, str)
        self.assertIsInstance(self.cityy.name, str)

    def test_has_attr(self):
        """some tests for instance of city"""
        self.assertTrue('id' in self.cityy.__dict__)
        self.assertTrue('created_at' in self.cityy.__dict__)
        self.assertTrue('updated_at' in self.cityy.__dict__)
        self.assertTrue('state_id' in self.cityy.__dict__)
        self.assertTrue('name' in self.cityy.__dict__)

    def test_save(self):
        """testing save method"""
        self.cityy.save()
        self.assertNotEqual(self.cityy.created_at, not (self.cityy.updated_at))

    def test_is_subclass(self):
        """Tests to see if City is a subclass of BaseModel"""
        ok = City()
        self.assertEqual(issubclass(type(ok), BaseModel), True)

    @classmethod
    def tearDown(self):
        """deletes self.cityy"""
        del self.cityy

if __name__ == "__main__":
    unittest.main()
