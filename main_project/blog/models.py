from django.db import models

# Create your models here.


class Post(models.Model):
    # TODO: adicionar o author
    title = models.CharField(max_length=200, blank=False)
    date = models.DateField(blank=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', default="default.png")
    excerpt = models.CharField(max_length=500,blank=True)
    content = models.TextField(blank=False)
    