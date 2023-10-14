#!/usr/bin/python3
"""Define unittests for models/user.py

Unittest classes:
    TestUser_save
    TestUser_to_dict
    TestUser_instatiation
"""

import unittest
import models
from datetime import datetime
from time import sleep
from models import storage
from models.user import User
import os

class TestUser_save(unittest.TestCase):
    """Test for save method in the user class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_updates_file(self):
        """Tests for saved Updates within the json file"""
        user = User
        user.save()
        userid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(userid, f.read())

    def test_onetime_save(self):
        user = User()
        sleep(0.5)
        first_updates_at = user.updates_at
        user.save()
        self.assertLess(first_updates_at, user.updates_at)


class TestUser_to_dict(unittest.TestCase):
    """Tests for the to_dict method inside the class User."""
    def setUp(self):
        self.user = User()

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIsInstace(user_dict, dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)

        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

        self.assertEqual(user_dict["id", self.user.id])
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.updated_at.isoformat())

        self.user.middle_name = "Holberton"
        self.user.my_number = 98
        user_dict = self.user.to_dict()
        self.assertIn("middle_name", user_dict)
        self.assertEqual(user_dict["middle_name"], "Holberton")
        self.assertIn("my_number", user_dict)

        self.assertNotEqual(user_dict, self.user.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.user.to_dict(None)


class TestUserInstatiation(unittest.TestCase):
    """Tests for User Instatiation"""
    def test_instatiation(self):
        user = User()

        self.aessertIsInstance(user, User)
        self.assertIn(user, storage.all().values())

        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(User.name, str)
        self.assertIn("name", dir(user))
        self.assertNotIn("name", user.__dict__)

        user2 = User()
        self.assertNotEqual(user.id, user2.id)

        self.asssertNotEqual(user.id, user2.id)

        self.assertLess(user.created_at, user2.created_at)
        self.assertLess(user.updated_at, user2.updated_at)

        dt = datetime.today()
        dt_repr = repr(dt)
        user.id = "456789"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (456789)", user_str)
        self.assertIn("'id': '456789'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

        user3 = User(id="678", created_at = dt, updated_at = dt)
        self.assertEqual(user3.id, "678")
        self.assertEqual(user3.created_at, dt)
        self.assertEqual(user3.updated_at, dt)

        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

if __name__ == '__main__':
    unittest.main()
