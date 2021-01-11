from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.france = Location.objects.create(country='France')
       
        self.gowns = Category.objects.create(name='gowns')
        self.jewells = Category.objects.create(name='jewells')

        self.shoes = Image.objects.create(
            name='shoes', location=self.france,  description='picture of a bride')

    
    def test_instance(self):
        self.shoes.save()
        self.assertTrue(isinstance(self.shoes, Image))

class CategoryTest(TestCase):
    def setUp(self):
        self.nature = Category(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))

class LocationTest(TestCase):
    def setUp(self):
        self.belgique = Location(country='Belgique')

    def test_instance(self):
        self.belgique.save()
        self.assertTrue(isinstance(self.belgique, Location))    
