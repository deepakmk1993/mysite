from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments")
    
    def __str__(self): 
        return self.title

admin.site.register(Post)
admin.site.register(Comment)