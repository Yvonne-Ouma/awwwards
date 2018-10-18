from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile , Project

# Create your tests here.

class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.yvonne = Profile(user = 'yvonne',user_name='yvonne',bio = 'this is true',profile_picture = 'gifts/media/profiles/anitaskitchen.jpg')
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.yvonne, Profile))
    #testing save method

    def test_save_method(self):
        self.yvonne.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    #testng for deleting method

    def test_delete_method(self):
        self.yvonne.save_profile()
        self.yvonne.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)



class ProjectTestClass(TestCase):
    def setUp(self):
        self.testuser=User(username="user",email="test@mail.com")

    def tearDown(self) :
        User.objects.all().delete()

                       