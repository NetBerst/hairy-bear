from django.db import models
from django.forms import ModelForm

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField("Дата публикации",auto_now_add=True)
    content = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class Comment(models.Model):
    autor = models.CharField(max_length=20)
    message = models.TextField(max_length=100)
    datetime = models.DateTimeField("Дата публикации",auto_now=True)
    post = models.ForeignKey(Post)    
 
    def __str__(self):
        return self.message

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['autor','message']
