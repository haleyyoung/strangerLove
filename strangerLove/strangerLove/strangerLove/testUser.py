from django.test import TestCase
from strangerLove.models import User

class AddUserTest(TestCase):
    def setUp(self):
        User.objects.create(firstName="Adam", lastName="Boot", email="adam.boot@test.com")

    def test_existence(self):
        user = User.objects.get(firstName="Adam")

        self.assertEqual(user.firstName, 'Adam')
        self.assertEqual(user.lastName, 'Boot')
        self.assertEqual(user.email, 'adam.boot@test.com')

class RemoveUserTest(TestCase):

    def setUp(self):
        User.objects.create(firstName="Adam", lastName="Boot", email="adam.boot@test.com")

    def test_existence(self):
        user = User.objects.get(firstName="Adam")

        self.assertEqual(user.firstName, 'Adam')
        self.assertEqual(user.lastName, 'Boot')
        self.assertEqual(user.email, 'adam.boot@test.com')

    def test_delete(self):
        user = User.objects.get(firstName="Adam")
        user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(firstName="Adam")