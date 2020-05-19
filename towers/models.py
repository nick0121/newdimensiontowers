import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from pages.choices import *




def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# Create your models here.
class Towers(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=False, default="this-is-a-slug")
    manufacturer = models.CharField(choices=MANUFACTURERS, default=None, max_length=50)
    start_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1970), max_value_current_year])
    end_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1970), max_value_current_year])
    model = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=False) 


    def get_name(self):
        name = self.manufacturer
        return name



    def first_image(self):
        main_image = Images.objects.filter(tower_id=self.id, orientation='main')
        return main_image[0]




    def get_absolute_url(self):
        return reverse('tower_product', kwargs={"manufacturer_name": self.manufacturer, "boat_id": self.slug}) 



    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Towers"



class TowerOrder(models.Model):

    name = models.CharField(max_length=100)
    tower = models.ForeignKey(Towers, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    style = models.CharField(max_length=2, choices=(('FL', 'Fullsize'), ('MN', 'Mini')), default='Fullsize')
    finish = models.CharField(max_length=20, choices=FINISHES, default=BRUSHED)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural = "TowerOrders"


class Biminis(models.Model):

    name = models.CharField(max_length=100)
    tower = models.ForeignKey(Towers, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Biminis"


class BiminiOrder(models.Model):

    name = models.CharField(max_length=100)
    bimini = models.ForeignKey(Biminis, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, choices=COLORS, default=COLORS[0])
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "BiminiOrders"


class Images(models.Model):

    title = models.CharField(max_length=100)
    tower = models.ForeignKey(Towers, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='images')
    product = models.ForeignKey('pages.Products', on_delete=models.CASCADE, blank=True, null=True, default=None)
    description = models.TextField(blank=True)
    manufacturer = models.CharField(choices=MANUFACTURERS, default=None, max_length=50)
    image = models.ImageField(upload_to='photos/')
    orientation = models.CharField(max_length=20, blank=True, default=None, choices=ORIENTATIONS)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Images"

