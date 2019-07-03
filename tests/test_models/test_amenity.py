#!/usr/bin/python3
"""
Unitesting amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Amenity(unittest.TestCase):
    """
    Unitesting Amenity class
    """
    @classmethod
    def setUpClass(self):
        """Setting it up"""
        self.mn = Amenity()
        self.mn.name = "Internet"

    def test_attr(self):
        """test attributes of Amenity"""
        self.assertTrue('name' in self.mn.__dict__)
        self.assertTrue('id' in self.mn.__dict__)
        self.assertTrue('created_at' in self.mn.__dict__)
        self.assertTrue('updated_at' in self.mn.__dict__)

    def test_to_dict(self):
        """test if to_dict function works"""
        self.assertEqual('to_dict' in dir(self.mn), True)

    def test_string(self):
        """test if Amenity is a string"""
        self.assertEqual(type(self.mn.name), str)

    def test_save(self):
        """testing save method"""
        self.mn.save()
        self.assertThat(self.mn.created_at, not (self.mn.updated_at))

    def test_not_none(self):
        """testing save method"""
        assertIsNotNone(self.pl)

    @classmethod
    def tearDownClass(self):
        """Tearing it all down by deletion"""
        del self.mn

if __name__ == "__main__":
    unittest.main()
