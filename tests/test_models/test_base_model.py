#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up an instance of BaseModel for testing"""
        self.base = BaseModel()

    def test_init(self):
        """Test that a new instance of BaseModel is correctly initialized"""
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        """Test that the string representation of a BaseModel instance is correct"""
        expected_output = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_output)

    def test_save(self):
        """Test that the save method correctly updates the updated_at attribute"""
        old_updated_at = self.base.updated_at
        self.base.save()
        new_updated_at = self.base.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a correct dictionary representation of a BaseModel instance"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(base_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], self.base.updated_at.isoformat())

    def test_init_kwargs(self):
        """Test that a new instance of BaseModel can be correctly initialized with kwargs"""
        base_dict = {'id': '1234-5678', 'created_at': '2022-11-11T11:11:11.111111', 'updated_at': '2022-11-11T11:11:11.111111'}
        base = BaseModel(**base_dict)
        self.assertEqual(base.id, '1234-5678')
        self.assertEqual(base.created_at, datetime.strptime('2022-11-11T11:11:11.111111', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(base.updated_at, datetime.strptime('2022-11-11T11:11:11.111111', '%Y-%m-%dT%H:%M:%S.%f'))


if __name__ == '__main__':
    unittest.main()

