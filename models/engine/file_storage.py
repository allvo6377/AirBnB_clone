#!/usr/bin/python3
"""A script that contains the FileStorage class"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = "{}"

    def all(self):
        """Returns the dictionary of objects"""
        return Filestorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of objects"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes object to JSON file"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name = value["__class__"]
                    cls = __import__("models").__dict__[class_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
