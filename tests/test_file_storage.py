#!/usr/bin/python3
""" file_storage
"""
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    """
    Create objects of FileStorage class.
    """
    def setUp(self):
        self.testa = FileStorage()
        self.testb = FileStorage()

    def test_attributes(self):
        """
        Test attributes of FileStorage.
        """

        self.assertTrue(hasattr(self.testa, "name"))
        self.assertTrue(hasattr(self.testb, "my_number"))
        self.assertTrue(hasattr(self.testa, "created_at"))
        self.assertTrue(hasattr(self.testa, "updated_at"))
        self.assertTrue(hasattr(self.testb, "id"))

    def test_save(self):
        """
        Test save method.
        """
        false_dict = {"id": {"__class__": "BaseModel"}}
        expect_dict = json.dumps(false_dict)
        self.assertTrue(type(expect_dict) is str)

    def reload(self):
        """
        Test reload method
        """
        false_val = {"id": {"__class__": "BaseModel"}}
        exp_val = json.loads(false_val)
        self.assertTrue(type(exp_val) is dict)

    def tearDown(self):
        """
        End of Unitestting
        """
        pass
