from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=2000)
    blog_creator = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


