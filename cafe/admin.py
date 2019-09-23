from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cafe)
admin.site.register(Review)
admin.site.register(Cafe_Like)
admin.site.register(Cafe_Unlike)
admin.site.register(Review_Like)
admin.site.register(Review_Unlike)
