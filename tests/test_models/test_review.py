#!/usr/bin/python3
"""Define unittests for models/review.py

Unittest classes:
    TestReview_save
    TestReview_to_dict
    TestReview_instatiation
"""

import unittest
import models
from datetime import datetime
from time import sleep
from models import storage
from models.review import Review
import os

class TestReview_save(unittest.TestCase):
    """Test for save method in the review class"""

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
        review = Review
        review.save()
        reviewid = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(reviewid, f.read())

    def test_onetime_save(self):
        review = Review()
        sleep(0.5)
        first_updates_at = review.updates_at
        review.save()
        self.assertLess(first_updates_at, review.updates_at)


class TestReview_to_dict(unittest.TestCase):
    """Tests for the to_dict method inside the class Review."""
    def setUp(self):
        self.review = Review()

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstace(review_dict, dict)
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)

        self.assertIsInstance(review_dict["id"], str)
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

        self.assertEqual(review_dict["id", self.review.id])
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["created_at"], self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"], self.review.updated_at.isoformat())

        self.review.middle_name = "Holberton"
        self.review.my_number = 98
        review_dict = self.review.to_dict()
        self.assertIn("middle_name", review_dict)
        self.assertEqual(review_dict["middle_name"], "Holberton")
        self.assertIn("my_number", review_dict)

        self.assertNotEqual(review_dict, self.review.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.review.to_dict(None)


class TestReviewInstatiation(unittest.TestCase):
    """Tests for Review Instatiation"""
    def test_instatiation(self):
        review = Review()

        self.aessertIsInstance(review, Review)
        self.assertIn(review, storage.all().values())

        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(Review.name, str)
        self.assertIn("name", dir(review))
        self.assertNotIn("name", review.__dict__)

        review2 = Review()
        self.assertNotEqual(review.id, review2.id)

        self.asssertNotEqual(review.id, review2.id)

        self.assertLess(review.created_at, review2.created_at)
        self.assertLess(review.updated_at, review2.updated_at)

        dt = datetime.today()
        dt_repr = repr(dt)
        review.id = "456789"
        review.created_at = review.updated_at = dt
        review_str = review.__str__()
        self.assertIn("[Review] (456789)", review_str)
        self.assertIn("'id': '456789'", review_str)
        self.assertIn("'created_at': " + dt_repr, review_str)
        self.assertIn("'updated_at': " + dt_repr, review_str)

        review3 = Review(id="678", created_at = dt, updated_at = dt)
        self.assertEqual(review3.id, "678")
        self.assertEqual(review3.created_at, dt)
        self.assertEqual(review3.updated_at, dt)

        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

if __name__ == '__main__':
    unittest.main()
