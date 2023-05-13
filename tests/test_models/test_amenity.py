#!/usr/bin/python3
"""Defines a set of unit tests for the Amenity model

This module contains a set of unit tests for the Amenity model.The tests ensure
that the model has the required attributes and methods, and that these behave
as expected.

The following tests are performed:
    - The Amenity instance has the required attributes.
    - The __str__ method returns the expected string representation.
    - The to_dict method returns a dictionary with the expected attributes.
    - The constructor properly initializes attributes from **kwargs.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines a set of unit tests for the Amenity model"""

    def setUp(self):
        """Creates a new instance of Amenity before each test"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Tests that the Amenity instance has the required attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str_method(self):
        """
        Tests that the __str__ method returns the expected
        string representation
        """
        expected = "[{}] ({}) {}".format(
            self.amenity.__class__.__name__,
            self.amenity.id,
            self.amenity.__dict__
        )
        self.assertEqual(str(self.amenity), expected)

    def test_to_dict_method(self):
        """
        Tests that the to_dict method returns a dictionary
        with the expected attributes
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["name"], self.amenity.name)
        self.assertEqual(
                amenity_dict["created_at"],
                self.amenity.created_at.isoformat())
        self.assertEqual(
                amenity_dict["updated_at"],
                self.amenity.updated_at.isoformat())
        self.assertEqual(
                amenity_dict["__class__"],
                self.amenity.__class__.__name__)

    def test_kwargs_constructor(self):
        """
        Tests that the constructor properly initializes attributes
        from **kwargs
        """
        kwargs = {
            "id": "test-id",
            "created_at": "2022-05-13T00:00:00.000000",
            "updated_at": "2022-05-13T00:00:00.000000",
            "name": "test-name",
        }
        amenity = Amenity(**kwargs)
        self.assertEqual(amenity.id, kwargs["id"])
        self.assertEqual(amenity.created_at.isoformat(), kwargs["created_at"])
        self.assertEqual(amenity.updated_at.isoformat(), kwargs["updated_at"])
        self.assertEqual(amenity.name, kwargs["name"])


if __name__ == '__main__':
    unittest.main()
