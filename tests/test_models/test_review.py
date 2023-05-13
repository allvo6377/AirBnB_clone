#!/usr/bin/python3
"""Tests for the Review class"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review model"""

    def test_init(self):
        """Test initialization of a Review instance"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_place_id(self):
        """Test setting the place ID of a Review instance"""
        review = Review()
        review.set_place_id("CA")
        self.assertEqual(review.place_id, "CA")
        self.assertEqual(review.get_place_id(), "CA")

    def test_set_user_id(self):
        """Test setting the user ID of a Review instance"""
        review = Review()
        review.set_user_id("1234567890")
        self.assertEqual(review.user_id, "1234567890")
        self.assertEqual(review.get_user_id(), "1234567890")

    def test_set_text(self):
        """Test setting the text of a Review instance"""
        review = Review()
        review.set_text("This is a nice place.")
        self.assertEqual(review.text, "This is a nice place.")
        self.assertEqual(review.get_text(), "This is a nice place.")


if __name__ == "__main__":
    unittest.main()
