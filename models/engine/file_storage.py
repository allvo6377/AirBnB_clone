#!/usr/bin/python3
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON
    file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        d = {}
        for key, value in FileStorage.__objects.items():
            d[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(d, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8" ) as f:
                d = json.load(f)
            for key, value in d.items():
                cls_name = value["__class__"]
                cls = eval(cls_name)
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            return
