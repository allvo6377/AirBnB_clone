#!/usr/bin/python3
"""Test suite for the Amenity class"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
"""Tests for the city class"""

    def test_init(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_set_state_id(self):
        city = City()
        city.set_state_id("CA")
        self.assertEqual(city.state_id, "CA")

    def test_set_name(self):
        city = City()
        city.set_name("San Francisco")
        self.assertEqual(city.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()
