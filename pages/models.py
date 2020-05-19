from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from localflavor.us.us_states import STATE_CHOICES
from phone_field import PhoneField
from .choices import *
from towers.models import Images





#CUSTOMER CLASS
class Customers(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    review = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        verbose_name_plural = "Customers"




## DEALER CLASS
class Dealers(models.Model):
    
    name = models.CharField(max_length=30)
    dealer_of = models.CharField("Manufacturer", max_length=100, choices=MANUFACTURERS)
    contactName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    has_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dealers"


# ADDRESS CLASS
class Address(models.Model):

    ''' Phone Number Format
        +[country code][number]x[extension]
        +12223334444x55 '''

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    dealer = models.ForeignKey(Dealers, on_delete=models.CASCADE, blank=True, null=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20)
    zipCode = models.CharField("Zip/Postal Code", max_length=20)
    phone = PhoneField(help_text='Contact phone number') 
    secondary_phone = PhoneField(blank=True, help_text='Secondary phone number') 
    country = CountryField(blank_label='(select country)')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address1


    class Meta:
        verbose_name_plural = "Addresses"
        



# Create your models here.
class Products(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField(default="url-slug")
    category = models.CharField("Category", max_length=50, choices=CATEGORY, default='accessory')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    length = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


    def first_image(self):
        main_image = Images.objects.filter(product_id=self.id)
        return main_image[0]


    def get_image(self):
        
        image = Images.objects.filter(product_id=self.id)
        return image[0]


    def get_absolute_url(self):
        return reverse('accessory_product', kwargs={"category": self.category, "id": self.slug}) 

    
    class Meta:
        verbose_name_plural = "Products"



class Orders(models.Model):

    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Orders"



class OrderDetails(models.Model):

    name = models.CharField(max_length=100)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    tower = models.ForeignKey('towers.TowerOrder', on_delete=models.CASCADE, null=True, blank=True)
    bimini = models.ForeignKey('towers.BiminiOrder', on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "OrderDetails"
        unique_together = ('order', 'product')

class Shipping(models.Model):

    # name = models.CharField(max_length=100)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    comments = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # def __str__(self):
    #     return self.order


    class Meta:
        verbose_name = "Shipping"


class Contact(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = PhoneField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.fullName
