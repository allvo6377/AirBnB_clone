#!/usr/bin/python3
"""Contains class BaseModel"""
from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    storage = FileStorage()

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        self.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
