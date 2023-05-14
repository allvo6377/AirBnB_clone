#!/usr/bin/python3
"""A module containing unit tests for the base_model class"""
import unittest
from datetime import datetime, timedelta
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(AttributeError):
            print(self.bm1.does_not_exist)

    def test_save(self):
        # Test calling the save method on a BaseModel instance
        bm = BaseModel()
        original_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(original_updated_at, bm.updated_at)

    def test_to_dict(self):
        # Test calling the to_dict method on a BaseModel instance
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)
        self.assertEqual(bm_dict["created_at"], str(bm.created_at.isoformat()))
        self.assertEqual(bm_dict["updated_at"], str(bm.updated_at.isoformat()))

        # Test calling the to_dict method with an argument
        with self.assertRaises(TypeError):
            bm.to_dict("invalid_arg")

    def test_equality(self):
        # Test equality and inequality of BaseModel instances
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertEqual(bm1, bm1)
        self.assertNotEqual(bm1, bm2)

    def test_created_at(self):
        # Test that the created_at attribute is set to the current datetime
        bm1 = BaseModel()
        now = datetime.now()
        self.assertLessEqual(bm1.created_at, now)
        self.assertGreaterEqual(bm1.created_at, now - timedelta(seconds=1))

    def test_updated_at(self):
        # Test that the updated_at attribute is set to the current datetime
        bm1 = BaseModel()
        now = datetime.now
