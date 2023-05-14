#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage and add some objects to it
        self.storage = FileStorage()
        self.user = User()
        self.state = State()
        self.storage.new(self.user)
        self.storage.new(self.state)

    def tearDown(self):
        # Delete the JSON file created by the tests
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        # Test that the 'all' method returns the correct dictionary of objects
        objs = self.storage.all()
        self.assertIn("User." + self.user.id, objs)
        self.assertIn("State." + self.state.id, objs)

    def test_new(self):
        # Test that the 'new' method adds an object to the dictionary of objects
        user2 = User()
        self.storage.new(user2)
        objs = self.storage.all()
        self.assertIn("User." + user2.id, objs)

    def test_save_reload(self):
        # Test that the 'save' method serializes the objects to the JSON file,
        # and that the 'reload' method deserializes the objects back into memory
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn("User." + self.user.id, data)
        self.assertIn("State." + self.state.id, data)
        self.storage = FileStorage()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIn("User." + self.user.id, objs)
        self.assertIn("State." + self.state.id, objs)
if __name__ == "__main__":
    unittest.main()
