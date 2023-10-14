#!/usr/bin/python3
"""Define unittests for models/city.py

Unittest classes:
    TestCity_save
    TestCity_to_dict
    TestCity_instatiation
"""

import unittest
import models
from datetime import datetime
from time import sleep
from models import storage
from models.city import City
import os

class TestCity_save(unittest.TestCase):
    """Test for save method in the city class"""

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
        city = City
        city.save()
        cityid = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(cityid, f.read())

    def test_onetime_save(self):
        city = City()
        sleep(0.5)
        first_updates_at = city.updates_at
        city.save()
        self.assertLess(first_updates_at, city.updates_at)


class TestCity_to_dict(unittest.TestCase):
    """Tests for the to_dict method inside the class City."""
    def setUp(self):
        self.city = City()

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstace(city_dict, dict)
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)

        self.assertIsInstance(city_dict["id"], str)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

        self.assertEqual(city_dict["id", self.city.id])
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.isoformat())

        self.city.middle_name = "Holberton"
        self.city.my_number = 98
        city_dict = self.city.to_dict()
        self.assertIn("middle_name", city_dict)
        self.assertEqual(city_dict["middle_name"], "Holberton")
        self.assertIn("my_number", city_dict)

        self.assertNotEqual(city_dict, self.city.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.city.to_dict(None)


class TestCityInstatiation(unittest.TestCase):
    """Tests for City Instatiation"""
    def test_instatiation(self):
        city = City()

        self.aessertIsInstance(city, City)
        self.assertIn(city, storage.all().values())

        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(City.name, str)
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

        city2 = City()
        self.assertNotEqual(city.id, city2.id)

        self.asssertNotEqual(city.id, city2.id)

        self.assertLess(city.created_at, city2.created_at)
        self.assertLess(city.updated_at, city2.updated_at)

        dt = datetime.today()
        dt_repr = repr(dt)
        city.id = "456789"
        city.created_at = city.updated_at = dt
        city_str = city.__str__()
        self.assertIn("[City] (456789)", city_str)
        self.assertIn("'id': '456789'", city_str)
        self.assertIn("'created_at': " + dt_repr, city_str)
        self.assertIn("'updated_at': " + dt_repr, city_str)

        city3 = City(id="678", created_at = dt, updated_at = dt)
        self.assertEqual(city3.id, "678")
        self.assertEqual(city3.created_at, dt)
        self.assertEqual(city3.updated_at, dt)

        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

if __name__ == '__main__':
    unittest.main()
