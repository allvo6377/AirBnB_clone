import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_email_attribute_cannot_be_null(self):
        user = User()
        user.email = None
        with self.assertRaises(ValueError):
            user.save()
   
   def test_password_attribute_cannot_be_null(self):
       user = User()
       user.password = None
       with self.assertRaises(ValueError):
           user.save()

    def test_get_all_users_returns_empty_list_if_no_users_exist(self):
        user_model = UserModel()
        users = user_model.get_all_users()
        self.assertEqual(users, [])

    def test_get_user_by_email_returns_none_if_user_does_not_exist(self):
        user_model = UserModel()
        user = user_model.get_user_by_email("email@example.com")
        self.assertIsNone(user)
    
    def test_delete_user_deletes_user_from_database(self):
        user_model = UserModel()
        user = User()
        user.email = "email@example.com"
        user_model.save(user)
        user_model.delete_user(user.email)
        user = user_model.get_user_by_email("email@example.com")
        self.assertIsNone(user)
    
    def test_user_class_is_robust_to_unexpected_input(self):
        user_model = UserModel()
        with self.assertRaises(ValueError):
            user_model.save(None)
    
    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_save(self):
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
