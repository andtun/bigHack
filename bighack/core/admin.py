from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


admin.site.register(Building)
admin.site.register(Application, inlines=[ImageInline])
admin.site.register(Image)
