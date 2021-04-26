import unittest
from app.models import User, Comment, Pitch

class CommentModelCase(unittest.TestCase):
    def setUp(self):
        self.user_Mary = User(username = 'Mary',password = 'testing', email = 'mary@testing.com')
        self.new_pitch = Pitch(post = 'some dummy pitch', user = self.user_Mary)
        self.new_comment = Comment(pitch_id = 15, content = "some comment")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.content,'some comment')
        self.assertEquals(self.new_comment.pitch_id, 15)

