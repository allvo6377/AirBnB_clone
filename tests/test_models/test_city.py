#!/usr/bin/python3
"""Test suite for the Amenity class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

if __name__ == '__main__':
    unittest.main()

