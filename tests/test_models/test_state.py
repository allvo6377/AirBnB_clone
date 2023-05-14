#!/usr/bin?python3
"""Unit tests for the State model and its functionality."""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test case class for the State model and its functionality."""

    def test_inheritance(self):
        """Test that a State object is an instance of the BaseModel class."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """
        Test that a State object has an attribute
        called name and its value is empty string.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_types(self):
        """Test that a State object's name attribute is of type string."""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_save(self):
        """
        Test that the save() method updates the updated_at
        attribute of a State object.
        """
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(old_updated_at, state.updated_at)

    def test_to_dict(self):
        """
        Test that the to_dict() method returns a
        dictionary representation of a State object.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
