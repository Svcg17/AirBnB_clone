#!/usr/bin/python3
"""
module test for place
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class Place(BaseModel):
    """Place class"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.pl = Place()

    def test_inst(self):
        """some tests for amenity"""
        ok = Place()
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

    def test_has_attr(self):
        """test for attributes"""
        self.assertTrue('id' in self.pl.__dict__)
        self.assertTrue('created_at' in self.pl.__dict__)
        self.assertTrue('updated_at' in self.pl.__dict__)
        self.assertTrue('city_id' in self.pl.__dict__)
        self.assertTrue('user_id' in self.pl.__dict__)
        self.assertTrue('name' in self.pl.__dict__)
        self.assertTrue('description' in self.pl.__dict__)
        self.assertTrue('number_rooms' in self.pl.__dict__)
        self.assertTrue('number_bathrooms' in self.pl.__dict__)
        self.assertTrue('max_guest' in self.pl.__dict__)
        self.assertTrue('price_by_night' in self.pl.__dict__)
        self.assertTrue('latitude' in self.pl.__dict__)
        self.assertTrue('longitude' in self.pl.__dict__)
        self.assertTrue('amenity_ids' in self.pl.__dict__)

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

    def test_save(self):
        """testing save method"""
        self.pl.save()
        self.assertThat(self.pl.created_at, not (self.pl.updated_at))

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
