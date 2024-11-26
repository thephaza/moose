from pyclbr import Class

from django.db import models

# Create your models here.
class Tag(models.Model):

    name = models.CharField(max_length=105)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=25)
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    text = models.TextField()
    author_name = models.CharField(max_length=25)
    author_position = models.CharField(max_length=25)
    author_image = models.ImageField(upload_to='posts/')
    is_published = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()

    is_visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=25, blank=True, null = True)
    message = models.TextField()

    is_solved = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name