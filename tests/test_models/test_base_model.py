#!/usr/bin/python3
"""A module containing unit tests for the base_model class"""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_with_kwargs(self):
        """Test initializing a BaseModel with kwargs"""
        kwargs = {"id": "test_id", "created_at": "2022-01-01T00:00:00.000000", "updated_at": "2022-01-01T00:00:00.000000", "test_attr": "test_value"}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, "test_id")
        self.assertEqual(bm.created_at, datetime(2022, 1, 1))
        self.assertEqual(bm.updated_at, datetime(2022, 1, 1))
        self.assertFalse(hasattr(bm, "test_attr"))
        self.assertIsNotNone(storage.all().get(bm.__class__.__name__ + "." + bm.id))

    def test_init_without_kwargs(self):
        """Test initializing a BaseModel without kwargs"""
        bm = BaseModel()
        self.assertIsNotNone(bm.id)
        self.assertIsNotNone(bm.created_at)
        self.assertIsNotNone(bm.updated_at)
        self.assertIsNotNone(storage.all().get(bm.__class__.__name__ + "." + bm.id))

    def test_init_with_invalid_kwargs(self):
        """Test initializing a BaseModel with invalid kwargs"""
        kwargs = {"invalid_key": "invalid_value"}
        bm = BaseModel(**kwargs)
        self.assertIsNotNone(bm.id)
        self.assertIsNotNone(bm.created_at)
        self.assertIsNotNone(bm.updated_at)
        self.assertIsNotNone(storage.all().get(bm.__class__.__name__ + "." + bm.id))

    def test_init_with_short_id(self):
        """Test initializing a BaseModel with a short id string"""
        bm = BaseModel(id="1234")
        self.assertEqual(len(bm.id), 36)

    def test_init_with_long_id(self):
        """Test initializing a BaseModel with a long id string"""
        bm = BaseModel(id="123456789012345678901234567890123456")
        self.assertEqual(len(bm.id), 36)

    def test_init_with_invalid_timestamp(self):
        """Test initializing a BaseModel with an invalid timestamp string"""
        kwargs = {"created_at": "2022-01-01", "updated_at": "2022-01-01"}
        bm = BaseModel(**kwargs)
        self.assertIsNotNone(bm.id)
        self.assertIsNotNone(bm.created_at)
        self.assertIsNotNone(bm.updated_at)
        self.assertIsNotNone(storage.all().get(bm.__class__.__name__ + "." + bm.id))

    def test_create_many_instances(self):
        """Test creating many BaseModel instances"""
        for i in range(10000):
            bm = BaseModel()
            self.assertIsNotNone(storage.all().get(bm.__class__.__name__ + "." + bm.id))

    def test_to_dict_with_all_attributes(self):
        """Test to_dict method with all BaseModel attributes"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict["__class__"], bm.__class__.__name__)
    
    def test_to_dict_with_extra_attributes(self):
        """Test to_dict method with extra attributes"""
        bm = BaseModel()
        bm.test_attr = "test_value"
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict["__class__"], bm.__class__.__name__)
        self.assertEqual(bm_dict["test_attr"], "test_value")


    def test_save_updates_timestamp(self):
        """Test that save method updates updated_at attribute"""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_save_saves_to_storage(self):
        """Test that save method saves instance to storage"""
        bm = BaseModel()
        bm.save()
        key = bm.__class__.__name__ + "." + bm.id
        self.assertIsNotNone(storage.all().get(key))

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        bm = BaseModel()
        expected = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected)


if __name__ == '__main__':
    unittest.main()
