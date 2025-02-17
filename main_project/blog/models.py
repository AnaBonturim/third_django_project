from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.caption
    
class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email_address = models.EmailField(blank=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.full_name()} ({self.email_address})"

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(auto_now=False, blank=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', default="default.png")
    excerpt = models.CharField(max_length=500,blank=True)
    content = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f"{self.title} ({self.author})"
    
    def tags_as_list(self):
        return self.tags.all()
    
    def has_tags(self):
        return len(self.tags_as_list()) > 0
 
    
class Comment(models.Model):
    content = models.TextField(blank=False, max_length=400)
    name = models.CharField(max_length=200, blank=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f"{self.content} ({self.name} with rating {self.rating})"
    
    def get_rating_range(self):
        return [ '#' for index in range(0,self.rating)]