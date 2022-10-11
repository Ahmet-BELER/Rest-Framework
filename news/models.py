from unicodedata import name
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=100)
    surname= models.CharField(max_length=100)
    biography= models.TextField()

    def __str__(self):
        return f'{self.name}  {self.surname}'


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE ,related_name='articles')
    header= models.CharField(max_length=100)
    explanation = models.CharField(max_length=100)
    text= models.TextField()
    city= models.CharField(max_length=100)
    release_date= models.DateField()
    active= models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.header  