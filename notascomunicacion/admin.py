from django.contrib import admin

# Register your models here.
from .models import NotaComunicacion

class NotaComunicacionAdmin(admin.ModelAdmin):
    list_display = ['asunto','resumen']

    pass
admin.site.register(NotaComunicacion, NotaComunicacionAdmin)
