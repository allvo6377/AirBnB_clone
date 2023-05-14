#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path: string - path to the JSON file.
        __objects: dictionary - empty but will store all objects by <class name>.id.

    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.load()

    def all(self):
        """Returns the dictionary `__objects`."""
        return self.__objects

    def new(self, obj):
        """Sets in `__objects` the obj with key `<obj class name>.id`."""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes `__objects` to the JSON file (`__file_path`)."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """Deserializes the JSON file (`__file_path`) to `__objects` (only if the JSON file (`__file_path`) exists; otherwise, do nothing. If the file doesn't exist, no exception should be raised)."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
