#!/usr/bin/python3
"""
Unitesting for review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """setting up test cases"""
        self.Joe = Review()
        self.Joe.place_id = "SF"
        self.Joe.user_id = "Decent"
        self.Joe.text = "Cloud"

    def test_has_att(self):
        """testing that attributes are true"""
        self.assertTrue('created_at' in self.Joe.__dict__)
        self.assertTrue('updated_at' in self.Joe.__dict__)
        self.assertTrue('place_id' in self.Joe.__dict__)
        self.assertTrue('text' in self.Joe.__dict__)
        self.assertTrue('id' in self.Joe.__dict__)
        self.assertTrue('user_id' in self.Joe.__dict__)

    def test_id(self):
        """ test id is correct """
        ok = Review()
        var = Review(ok)
        self.assertEqual(str, type(ok.id))
        self.assertEqual(type(var), Review)

    def test_attri(self):
        """Do all required functions exist"""
        self.assertTrue(hasattr(Review, "__str__"))
        self.assertTrue(hasattr(Review, "to_dict"))
        self.assertFalse(hasattr(Review, "name"))
        self.assertTrue(hasattr(Review, "save"))
        self.assertTrue(hasattr(Review, "__class__"))

    def test_string(self):
        """testing that it's a string"""
        ok = Review()
        self.assertEqual(type(ok.place_id), str)
        self.assertEqual(type(ok.user_id), str)
        self.assertEqual(type(ok.text), str)

    def test_to_dict(self):
        """testing that to_dict method functions"""
        self.assertEqual('to_dict' in dir(self.Joe), True)

    def test_creat_update(self):
        """ test updated_at and updated_at """
        ok = Review()
        self.assertEqual(datetime, type(ok.created_at))
        self.assertEqual(datetime, type(ok.updated_at))

    def test_save(self):
        """testing save method"""
        self.Joe.save()
        self.assertNotEqual(self.Joe.created_at, self.Joe.updated_at)

    @classmethod
    def tearDownClass(self):
        """deletes self.Joe"""
        del self.Joe

if __name__ == "__main__":
    unittest.main()
