from django.contrib import admin
from .models import Pdx


class PdxAdmin(admin.ModelAdmin):
    pdx = '__all__'

    admin.site.register(Pdx)

