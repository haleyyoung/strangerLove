from django.test import TestCase
from strangerLove.models import User

class AddUserTest():
    def create(self):
        User.objects.create(firstName="Adam", lastName="Boot", email="adam.boot@test.com")

    def test_existence(self):
        user = User.objects.get(firstName="Adam")

        self.assertEqual(user.firstName, 'Adam')
        self.assertEqual(user.LastName, 'Boot')
        self.assertEqual(user.email, 'adam.boot@test.com')

class RemoveUserTest():

    def create(self):
        User.objects.create(firstName="Adam", lastName="Boot", email="adam.boot@test.com")

    def test_existence(self):
        user = User.objects.get(firstName="Adam")

        self.assertEqual(user.firstName, 'Adam')
        self.assertEqual(user.LastName, 'Boot')
        self.assertEqual(user.email, 'adam.boot@test.com')

    def delete(self):
        user = User.objects.get(firstName="Adam")
        user.delete()

    def test_non_existence(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(firstName="Adam")