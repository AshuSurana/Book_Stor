from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Books(models.Model):
    title= models.CharField(max_length=264)
    author = models.CharField(max_length=264)
    category = models.ManyToManyField(Category,related_name='Books')
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.IntegerField()
    publication_date = models.DateField()
    cover_image = models.ImageField()

    def __str__(self):
        return self.title

    

