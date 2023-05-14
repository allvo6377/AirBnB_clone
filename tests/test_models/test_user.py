#!/usr/bin/python3
"""Tests for the user class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
