from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=300)
    text=RichTextUploadingField(blank=True,null=True)
    image = models.FileField(blank=True)
    pin_to_bio = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField()

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Slideshow(models.Model):
    image = models.FileField(upload_to = 'slideshow/')


class Message(models.Model):
    title = models.CharField(max_length = 200,blank=True)
    text = RichTextUploadingField(blank = True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
