#!/usr/bin/python3
"""Tests for the class Place"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        self.place = Place()

    def test_init(self):
        """Test initialization of Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_set_city_id(self):
        """Test setting city_id attribute"""
        place = Place()
        place.set_city_id("CA")
        self.assertEqual(place.city_id, "CA")

    def test_set_user_id(self):
        """Test setting user_id attribute"""
        place = Place()
        place.set_user_id("1234567890")
        self.assertEqual(place.user_id, "1234567890")

    def test_set_name(self):
        """Test setting name attribute"""
        place = Place()
        place.set_name("San Francisco")
        self.assertEqual(place.name, "San Francisco")

    def test_set_description(self):
        """Test setting description attribute"""
        place = Place()
        place.set_description("This is a nice place.")
        self.assertEqual(place.description, "This is a nice place.")

    def test_set_number_rooms(self):
        """Test setting number_rooms attribute"""
        place = Place()
        place.set_number_rooms(3)
        self.assertEqual(place.number_rooms, 3)

    def test_set_number_bathrooms(self):
        """Test setting number_bathrooms attribute"""
        place = Place()
        place.set_number_bathrooms(2)
        self.assertEqual(place.number_bathrooms, 2)

    def test_set_max_guest(self):
        """Test setting max_guest attribute"""
        place = Place()
        place.set_max_guest(4)
        self.assertEqual(place.max_guest, 4)

    def test_set_price_by_night(self):
        """Test setting price_by_night attribute"""
        place = Place()
        place.set_price_by_night(100)
        self.assertEqual(place.price_by_night, 100)

    def test_set_latitude(self):
        """Test setting latitude attribute"""
        place = Place()
        place.set_latitude(37.775)
        self.assertEqual(place.latitude, 37.775)

    def test_set_longitude(self):
        """Test setting longitude attribute"""
        place = Place()
        place.set_longitude(-122.4189)
        self.assertEqual(place.longitude, -122.4189)

    def test_set_amenity_ids(self):
        """Test setting amenity_ids attribute"""
        place = Place()
        place.set_amenity_ids([1, 2, 3])
        self.assertEqual(place.amenity_ids, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
