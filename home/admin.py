from django.contrib import admin
from .models import States, Regions, SubRegions, Comment
from .models import Product

# Register your models here.
admin.site.register(States)
admin.site.register(Regions)
admin.site.register(SubRegions)
admin.site.register(Product)
admin.site.register(Comment)