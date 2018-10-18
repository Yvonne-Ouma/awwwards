from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project,Review

# Create your tests here.

class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.yvonne = Profile(user_name='yvonne',bio = "good",profile_picture = "gifts/media/profiles/ttt.jpg")
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.yvonne, Profile))
#     #testing save method

    def test_save_method(self):
        self.yvonne.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_method(self):
        self.yvonne.save()
        self.yvonne.delete()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) == 1)



class ProjectTestClass(TestCase):
    def setUp(self):
        self.projectTest=Project(name="blog",photo="gifts/media/images/blog.jpg",project_description="a better experience", project_url="https://moringaschool.instructure.com", technologies_used = "html")

#     def tearDown(self) :
#         User.objects.all().delete()

    def test_instance(self):
        self.assertIsInstance(self.projectTest,Project)

    def test_save_project(self):
        self.assertFalse(self.projectTest in Project.objects.all())
        self.projectTest.save()
        self.assertTrue(self.projectTest in Project.objects.all())
        self.projectTest.delete()

    def test_delete_project(self):
        self.assertFalse(self.projectTest in Project.objects.all())
        self.projectTest.save()
        self.assertTrue(self.projectTest in Project.objects.all())
        self.projectTest.delete()


class ReviewTestClass(TestCase):
    def setUp(self):
        self.review=Review(comment="wooowww....",design=4,usability= 6, content=7)

#     def tearDown(self) :
#         Review.objects.all().delete()

#     def test_instance(self):
#         self.assertIsInstance(self.review,Review)

#     def test_save_review(self):
#         self.assertFalse(self.review in Review.objects.all())
#         self.review.save()
#         self.assertTrue(self.review in Review.objects.all())
#         self.review.delete()

#     def test_delete_review(self):
#         self.assertTrue(self.review in Review.objects.all())
#         self.review.save()
#         self.assertFalse(self.review in Review.objects.all())
#         self.review.delete()


                     