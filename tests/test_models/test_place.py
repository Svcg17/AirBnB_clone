#!/usr/bin/python3
"""
module test for place
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class Test_place(unittest.TestCase):
    """Place class"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.pl = Place()

    def test_type(self):
        """Testing for type of instance place
        """
        self.assertTrue(type(self.pl), Place)

    def test_hasattr(self):
        """Testing if isntance has attribute
        """
        self.assertTrue(hasattr(self.pl, "city_id"))
        self.assertTrue(hasattr(self.pl, "user_id"))
        self.assertTrue(hasattr(self.pl, "name"))
        self.assertTrue(hasattr(self.pl, "description"))
        self.assertTrue(hasattr(self.pl, "number_rooms"))
        self.assertTrue(hasattr(self.pl, "number_bathrooms"))
        self.assertTrue(hasattr(self.pl, "max_guest"))
        self.assertTrue(hasattr(self.pl, "price_by_night"))
        self.assertTrue(hasattr(self.pl, "latitude"))
        self.assertTrue(hasattr(self.pl, "longitude"))
        self.assertTrue(hasattr(self.pl, "amenity_ids"))

    def test_inst(self):
        """some tests for amenity"""
        ok = Place()
        self.assertEqual(issubclass(type(ok), BaseModel), True)
        self.assertIsInstance(ok, Place)
        self.assertIsInstance(ok.city_id, str)
        self.assertIsInstance(ok.user_id, str)
        self.assertIsInstance(ok.name, str)
        self.assertIsInstance(ok.description, str)
        self.assertIsInstance(ok.number_rooms, int)
        self.assertIsInstance(ok.number_bathrooms, int)
        self.assertIsInstance(ok.max_guest, int)
        self.assertIsInstance(ok.price_by_night, int)
        self.assertIsInstance(ok.latitude, float)
        self.assertIsInstance(ok.longitude, float)
        self.assertIsInstance(ok.amenity_ids, list)

    def test_to_dict(self):
        """test to_dict function is working"""
        self.assertEqual('to_dict' in dir(self.pl), True)

    def test_dict_to(self):
        """ test if dictionary"""
        ok = Place()
        var = ok.to_dict()
        foo = Place(var)
        self.assertEqual(type(var), dict)
        self.assertTrue(hasattr(foo, "__class__"))
        self.assertTrue(hasattr(foo, "__str__"))
        self.assertTrue(hasattr(foo, "to_dict"))
        self.assertTrue(hasattr(foo, "name"))
        self.assertTrue(hasattr(foo, "save"))
        self.assertTrue(hasattr(foo, "__class__"))

    def test_creat_and_update(self):
        """ test created_at and updated at the same time"""
        ok = Place()
        self.assertEqual(datetime, type(ok.created_at))
        self.assertEqual(datetime, type(ok.updated_at))

    def test_id(self):
        """ test id is correct"""
        ok = Place()
        self.assertEqual(str, type(ok.id))
        self.assertEqual(type(ok), Place)

    @classmethod
    def tearDown(self):
        """deletes place"""
        del self.pl

if __name__ == "__main__":
    unittest.main()
