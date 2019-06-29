import unittest
import datetime
from models.base_model import BaseModel

class TestBase(unittest.TestBase):
    """Tests for base"""

    def setUp(self):
        self.a = BaseModel()
        self.b = BaseModel()

    def test_if_true(self):
    """Test if true"""
        self.assert

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
