from django.db import models
from blog.models.category import Category

class Post(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='media/images/')
    author = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title