from django.db import models
import datetime as dt

# Create your models here.
class Locatio(models.Model):
    country = models.CharField(max_length =30)
    city = models.CharField(max_length =30)
    def __str__(self):
        return self.country
    def save_category(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length =30) 
    def __str__(self):
        return self.category    

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()  
    @classmethod
    def get_image(cls,id):
        try:
            image=Image.objects.get(id=id)
            return image
        except DoesNotExist:
            return Image.objects.get(id=1) 
    @classmethod
    def search_by_category(cls, search_term):
        display = cls.objects.filter(category__name__icontains=search_term)
        return display     
    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location
    @classmethod
    def view_category(cls,cat):
        image_category = cls.objects.filter(image_category=cat)
        return image_category    
