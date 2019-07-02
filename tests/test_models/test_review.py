#!/usr/bin/python3
"""
Unitesting for review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


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

    def test_string(self):
        """testing that it's a string"""
        self.assertEqual(type(self.Joe.place_id), str)
        self.assertEqual(type(self.Joe.user_id), str)
        self.assertEqual(type(self.Joe.text), str)

    def test_to_dict(self):
        """testing that to_dict method functions"""
        self.assertEqual('to_dict' in dir(self.Joe), True)

    @classmethod
    def tearDownClass(self):
        """deletes self.Joe"""
        del self.Joe

if __name__ == "__main__":
    unittest.main()
