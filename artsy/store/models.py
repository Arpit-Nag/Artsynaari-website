from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import Customer
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField
# from colorfield.fields import ColorField

class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

# class YarnColor(models.Model):
#     available_colors = ColorField()
#
#
#     def __str__(self):
#         return self.available_colors


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to='thumbnails/',blank=True)
    created_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse('store:product_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.product.title


class ProductRequest(models.Model):
    states=[
        ('State','State'),
        ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chandigarh','Chandigarh'),
        ('Chhattisgarh','Chhattisgarh'),
        ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
        ('Daman and Diu','Daman and Diu'),
        ('Delhi','Delhi'),
        ('Goa','Goa'),
        ('Gujrat','Gujrat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Jammu and Kashmir','Jammu and Kashmir'),
        ('Jharkhand','Jharkhand'),
        ('Karnataka','Karnataka'),
        ('Kerla','Kerla'),
        ('Ladakh','Ladakh'),
        ('Lakshadweep','Lakshadweep'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),
        ('Meghalaya','Meghalaya'),
        ('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),
        ('Odisha','Odisha'),
        ('Puducherry','Puducherry'),
        ('Punjab','Punjab'),
        ('Rajasthan','Rajasthan'),
        ('Sikkim','Sikkim'),
        ('Tamil Nadu','Tamil Nadu'),
        ('Telangana','Telangana'),
        ('Tripura','Tripura'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Uttarakhand','Uttarakhand'),
        ('West Bengal','West Bengal'),
    ]
    sizes = [('2XS','2XS'),
             ('XS','XS'),
             ('S','S'),
             ('M','M'),
             ('L','L'),
             ('XL','XL'),
             ('2XL','2XL'),
             ('3XL','3XL'),
             ('4XL','4XL'),
             ('Made to measure','Made to measure')
             ]
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    payment_status = models.BooleanField(default=False)
    discription = models.TextField(blank=True,null=True)
    size = models.CharField(max_length = 50, choices = sizes,null=True)
    request_date= models.DateTimeField(default = timezone.now)
    local_address = models.TextField()
    city = models.CharField(max_length = 200)
    district = models.CharField(max_length = 200)
    state = models.CharField(max_length = 100,choices=states)
    pin = models.CharField(max_length = 200)
    contact = models.IntegerField()

    def assigned_slot(self):
        return self.slot.get()

    def get_absolute_url(self):
        return reverse('store:request_summary',kwargs={'pk':self.pk})

    def __str__(self):
        s=self.customer.first_name+" "+self.customer.last_name+", "+self.product.title
        return s


class Slot(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    starting_date = models.DateField()
    ending_date=models.DateField(default=None)
    request_slot = models.ForeignKey(ProductRequest,related_name = 'slot',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.starting_date)+'---'+str(self.ending_date)+' / '+str(self.category)


class yarn(models.Model):
    material = models.CharField(max_length = 100)
    color_name = models.CharField(max_length=100,default='SOME STRING')
    color = ColorField()

    def __str__(self):
        s=self.material+","+self.color_name
        return s

class Muses(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True,default=None)
    thumbnail = models.FileField(upload_to='muses_thumbnail/',default=None)

    def __str__(self):
        return self.name


class MusesImage(models.Model):
    model = models.ForeignKey(Muses,on_delete=models.CASCADE,default=None)
    image = models.FileField(upload_to='muses/')

    def __str__(self):
        return self.model.name
