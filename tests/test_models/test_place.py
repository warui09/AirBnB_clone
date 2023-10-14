#!/usr/bin/python3
"""Define unittests for models/place.py

Unittest classes:
    TestPlace_save
    TestPlace_to_dict
    TestPlace_instatiation
"""

import unittest
import models
from datetime import datetime
from time import sleep
from models import storage
from models.place import Place
import os

class TestPlace_save(unittest.TestCase):
    """Test for save method in the place class"""

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
        place = Place
        place.save()
        placeid = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(placeid, f.read())

    def test_onetime_save(self):
        place = Place()
        sleep(0.5)
        first_updates_at = place.updates_at
        place.save()
        self.assertLess(first_updates_at, place.updates_at)


class TestPlace_to_dict(unittest.TestCase):
    """Tests for the to_dict method inside the class Place."""
    def setUp(self):
        self.place = Place()

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstace(place_dict, dict)
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)

        self.assertIsInstance(place_dict["id"], str)
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

        self.assertEqual(place_dict["id", self.place.id])
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["created_at"], self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], self.place.updated_at.isoformat())

        self.place.middle_name = "Holberton"
        self.place.my_number = 98
        place_dict = self.place.to_dict()
        self.assertIn("middle_name", place_dict)
        self.assertEqual(place_dict["middle_name"], "Holberton")
        self.assertIn("my_number", place_dict)

        self.assertNotEqual(place_dict, self.place.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.place.to_dict(None)


class TestPlaceInstatiation(unittest.TestCase):
    """Tests for Place Instatiation"""
    def test_instatiation(self):
        place = Place()

        self.aessertIsInstance(place, Place)
        self.assertIn(place, storage.all().values())

        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(Place.name, str)
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

        place2 = Place()
        self.assertNotEqual(place.id, place2.id)

        self.asssertNotEqual(place.id, place2.id)

        self.assertLess(place.created_at, place2.created_at)
        self.assertLess(place.updated_at, place2.updated_at)

        dt = datetime.today()
        dt_repr = repr(dt)
        place.id = "456789"
        place.created_at = place.updated_at = dt
        place_str = place.__str__()
        self.assertIn("[Place] (456789)", place_str)
        self.assertIn("'id': '456789'", place_str)
        self.assertIn("'created_at': " + dt_repr, place_str)
        self.assertIn("'updated_at': " + dt_repr, place_str)

        place3 = Place(id="678", created_at = dt, updated_at = dt)
        self.assertEqual(place3.id, "678")
        self.assertEqual(place3.created_at, dt)
        self.assertEqual(place3.updated_at, dt)

        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

if __name__ == '__main__':
    unittest.main()
