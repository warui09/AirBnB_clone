#!/usr/bin/python3
"""Define unittests for models/amenity.py

Unittest classes:
    TestAmenity_save
    TestAmenity_to_dict
    TestAmenity_instatiation
"""

import unittest
import models
from datetime import datetime
from time import sleep
from models import storage
from models.amenity import Amenity
import os

class TestAmenity_save(unittest.TestCase):
    """Test for save method in the amenity class"""

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
        amen = Amenity
        amen.save()
        amenid = "Amenity." + amen.id
        with open("file.json", "r") as f:
            self.assertIn(amenid, f.read())

    def test_onetime_save(self):
        amen = Amenity()
        sleep(0.5)
        first_updates_at = amen.updates_at
        amen.save()
        self.assertLess(first_updates_at, amen.updates_at)


class TestAmenity_to_dict(unittest.TestCase):
    """Tests for the to_dict method inside the class Amenity."""
    def setUp(self):
        self.amen = Amenity()

    def test_to_dict(self):
        amen_dict = self.amen.to_dict()
        self.assertIsInstace(amen_dict, dict)
        self.assertIn("id", amen_dict)
        self.assertIn("created_at", amen_dict)
        self.assertIn("updated_at", amen_dict)
        self.assertIn("__class__", amen_dict)

        self.assertIsInstance(amen_dict["id"], str)
        self.assertIsInstance(amen_dict["created_at"], str)
        self.assertIsInstance(amen_dict["updated_at"], str)

        self.assertEqual(amen_dict["id", self.amen.id])
        self.assertEqual(amen_dict["__class__"], "Amenity")
        self.assertEqual(amen_dict["created_at"], self.amen.created_at.isoformat())
        self.assertEqual(amen_dict["updated_at"], self.amen.updated_at.isoformat())

        self.amen.middle_name = "Holberton"
        self.amen.my_number = 98
        amen_dict = self.amen.to_dict()
        self.assertIn("middle_name", amen_dict)
        self.assertEqual(amen_dict["middle_name"], "Holberton")
        self.assertIn("my_number", amen_dict)

        self.assertNotEqual(amen_dict, self.amen.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.amen.to_dict(None)


class TestAmenityInstatiation(unittest.TestCase):
    """Tests for AMenity Instatiation"""
    def test_instatiation(self):
        amenity = Amenity()

        self.aessertIsInstance(amenity, Amenity)
        self.assertIn(amenity, storage.all().values())

        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(Amenity.name, str)
        self.assertIn("name", dir(amenity))
        self.assertNotIn("name", amenity.__dict__)

        amenity2 = Amenity()
        self.assertNotEqual(amenity.id, amenity2.id)

        self.asssertNotEqual(amenity.id, amenity2.id)

        self.assertLess(amenity.created_at, amenity2.created_at)
        self.assertLess(amenity.updated_at, amenity2.updated_at)

        dt = datetime.today()
        dt_repr = repr(dt)
        amenity.id = "456789"
        amenity.created_at = amenity.updated_at = dt
        amen_str = amenity.__str__()
        self.assertIn("[Amenity] (456789)", amen_str)
        self.assertIn("'id': '456789'", amen_str)
        self.assertIn("'created_at': " + dt_repr, amen_str)
        self.assertIn("'updated_at': " + dt_repr, amen_str)

        amenity3 = Amenity(id="678", created_at = dt, updated_at = dt)
        self.assertEqual(amenity3.id, "678")
        self.assertEqual(amenity3.created_at, dt)
        self.assertEqual(amenity3.updated_at, dt)

        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == '__main__':
    unittest.main()