""" Unittest for BaseModel class
"""
import unittest
import sys
import os
import json
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel


class Test_Base_Model(unittest.TestCase):
    """Tests for base
    """

    def setUp(self):
        """setUp for Base Model
        """
        self.a = BaseModel()
        self.b = BaseModel()

    def test_assignment(self):
        """Testing for BaseModel instance creation
        """
        outvar = StringIO()
        sys.stdout = outvar
        b = BaseModel()
        b.name = "Holberton"
        b.my_num = 87
        kwargs = {'lastname': "Sneha", 'key': 1234}
        c = BaseModel(**kwargs)
        self.assertTrue(type(b), BaseModel)
        kwargss = {}
        d = BaseModel(kwargss)
        print(b.name)
        print(b.my_num)
        sys.stdout = sys.__stdout__
        self.assertTrue(hasattr(b, "name"))
        self.assertTrue(hasattr(b, "my_num"))
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(b.name, "Holberton\n")
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertEqual(outvar.getvalue(), "Holberton\n87\n")
        json_model = b.to_dict()
        json_model = b.save()

    def test_attr(self):
        """Testing for attributes of new instances
        """
        new = BaseModel()
        self.assertTrue(new.id)
        self.assertTrue(new.updated_at)
        self.assertTrue(new.created_at)

    def test_errors_methods(self):
        """Testing for parameter errors
        """
        ins = BaseModel()
        with self.assertRaises(TypeError):
            new = BaseModel(**"sddsf")
            newer = BaseModel(**[])
            newerer = BaseModel(**123)
            new = BaseModel(**234.423)
            new = BaseModel((2, 4), (3, 4))
            ins.save("sdf")
            ins.save(1234)
            ins.save({})
            ins.save([2, 2, 2, 2])
            ins.save([])
            ins.save({'sdf': "sadf", 'aesdf': '234'})
            ins.save((1)(1)(1))
            ins.save(234.44)
            ins.to_dict("asdf")
            ins.to_dict([2, 2, 2])
            ins.to_dict((2, 3), (3, 3))
            ins.to_dict({})
            ins.to_dict(124)
            ins.to_dictt(1234.4)

    def test_name_errors(self):
        """Testing for name errors
        """
        ins = BaseModel()
        with self.assertRaises(NameError):
            ins.save(fasfsadf)
            ins.to_dict(asdf)

    def test_datetime(self):
        """Testing time difference when creating and updating instance
        """
        c = BaseModel()
        date = datetime.now()
        time_diff = c.updated_at - c.created_at
        self.assertTrue(abs(time_diff.total_seconds()) < 0.01)
        time_diff_two = c.created_at - c.updated_at
        self.assertTrue(abs(time_diff_two.total_seconds()) < 0.01)

    def test_format(self):
        """checks correct format"""
        self.assertRegex(self.a.__str__(), '\[.*\]\s+\(.*\)\s+\{.*\}')

    def test_to_dict(self):
        """test to_dict"""
        self.assertIsInstance(self.a, BaseModel)
        self.assertIsInstance(self.b, BaseModel)

    @classmethod
    def tearDown(self):
        """Tests for TearDown"""
        pass
