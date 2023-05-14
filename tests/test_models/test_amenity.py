#!/usr/bin/python3
"""Defines a set of unit tests for the Amenity model"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTests(unittest.TestCase):

    def test_name(self):
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")


if __name__ == "__main__":
    unittest.main()
