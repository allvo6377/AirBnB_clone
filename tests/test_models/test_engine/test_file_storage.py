#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os.path

import models
from models import base_model
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage



class TestFileStorage(unittest.TestCase):

    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Sets up the test environment."""
        self.file_storage = FileStorage()

    def test_all(self):
        """Tests that the all() method returns an empty dictionary."""
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """Tests that the new() method adds a new object to the dictionary of objects."""
        user = User("johndoe", "johndoe@example.com", "password")
        self.file_storage.new(user)
        self.assertEqual(self.file_storage.all()["User.1"], user)

    def test_save(self):
        """Tests that the save() method serializes the object to a JSON file."""
        user = User("johndoe", "johndoe@example.com", "password")
        self.file_storage.new(user)
        self.file_storage.save()
        with open("file.json", "r") as f:
            json_dict = json.load(f)
            self.assertEqual(json_dict["User.1"], user.to_dict())

    def test_reload(self):
        """Tests that the reload() method deserializes the JSON file to objects."""
        user = User("johndoe", "johndoe@example.com", "password")
        self.file_storage.new(user)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all()["User.1"], user)

    def test_add_existing_object(self):
        """Tests that the new() method raises an exception if you try to add an object that already exists in the database."""
        user = User("johndoe", "johndoe@example.com", "password")
        self.file_storage.new(user)
        with self.assertRaises(Exception):
            self.file_storage.new(user)

    def test_save_invalid_object(self):
        """Tests that the save() method raises an exception if you try to save an object that is not a valid model."""
        with self.assertRaises(Exception):
            self.file_storage.save({})

    def test_reload_missing_file(self):
        """Tests that the reload() method raises an exception if the JSON file is missing."""
        with self.assertRaises(FileNotFoundError):
            self.file_storage.reload()


if __name__ == "__main__":
    unittest.main()
