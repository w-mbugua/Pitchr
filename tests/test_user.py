import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    
    def setUp(self):
        self.new_user = User(password = 'password')
        self.new_user2 = User(password = 'password')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
    
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('password'))
        self.assertFalse(self.new_user.verify_password('testing'))
    
    def test_password_salts_are_random(self):
        self.assertTrue(self.new_user.password_hash != self.new_user2.password_hash)