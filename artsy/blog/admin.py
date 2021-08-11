from django.contrib import admin
from .models import Post,Category,Slideshow,Message
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Slideshow)
