from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from towers.models import Towers
# from .models import Products


class StaticViewSitemap(Sitemap):
    priority = "0.9"
    changefreq = "weekly"

    def items(self):
        return ['index', 'about', 'towers', 'contact', 'accessories', 'biminis']

    
    def location(self, item):
        return reverse(item)


# class ProductSitemap(Sitemap):
#     changefreq = "daily"
#     priority = "0.8"

#     def items(self):
#         return Products.objects.all()



class TowersSitemap(Sitemap):
    changefreq = "daily"
    priority = "0.8"


    def items(self):
        return Towers.objects.all()

