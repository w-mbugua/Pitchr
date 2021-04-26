import unittest
from app.models import User, Pitch

class PitchModelCase(unittest.TestCase):
    def setUp(self):
        self.user_Mary = User(username = 'Mary',password = 'testing', email = 'mary@testing.com')
        self.new_pitch = Pitch(post = 'some dummy pitch', user = self.user_Mary)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.post,'some dummy pitch')
        self.assertEquals(self.new_pitch.user,self.user_Mary)
