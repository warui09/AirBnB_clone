#!/usr/bin/python3
"""
Tests for the BaseModel class
"""

from models.base_model1 import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test initialization of the BaseModel class
    """

    def test_id(self):
        """
        Test if initialized instance has id
        """
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(isinstance(a.id, str))

    def test_created_at(self):
        """
        Test if created_at is initialized with a valid datetime object
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, "created_at"))
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at(self):
        """
        Test if updated_at is initialized with a valid datetime object
        """
        a = BaseModel()
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertIsInstance(a.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
