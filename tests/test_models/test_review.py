#!/usr/bin/python3
"""Tests for the Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
