from django.db import models
from taggit.managers import TaggableManager

# Create your models here.    

class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    publication_date = models.DateField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/', default='static/blog/tenor.gif')
    tags = TaggableManager()

    def __str__(self) -> str:
        return f"{self.title} on {self.publication_date}"
    
    # 1NF 2NF 3NF

class Review(models.Model):
    title_review = models.CharField(max_length=60)
    date_review = models.DateField(auto_now=True)
    comment = models.TextField()
    notation = models.IntegerChoices('Notation', '1 2 3 4 5')
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    # 1NF 2NF 3NF



