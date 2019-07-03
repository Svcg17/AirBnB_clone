#!/usr/bin/python3
"""
module test for place
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class Place(BaseModel):
    """Place class"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.pl = Place()

    def test_inst(self):
        """some tests for amenity"""
        self.assertIsInstance(self.pl, Place)
        self.assertIsInstance(self.pl.city_id, str)
        self.assertIsInstance(self.pl.user_id, str)
        self.assertIsInstance(self.pl.name, str)
        self.assertIsInstance(self.pl.description, str)
        self.assertIsInstance(self.pl.number_rooms, int)
        self.assertIsInstance(self.pl.number_bathrooms, int)
        self.assertIsInstance(self.pl.max_guest, int)
        self.assertIsInstance(self.pl.price_by_night, int)
        self.assertIsInstance(self.pl.latitude, float)
        self.assertIsInstance(self.pl.longitude, float)
        self.assertIsInstance(self.pl.amenity_ids, list)

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

    def test_save(self):
        """testing save method"""
        self.pl.save()
        self.assertThat(self.pl.created_at, not (self.pl.updated_at))

    def test_not_none(self):
        """testing save method"""
        assertIsNotNone(self.pl) 

    @classmethod
    def tearDown(self):
        """deletes place"""
        del self.pl

if __name__ == "__main__":
    unittest.main()
