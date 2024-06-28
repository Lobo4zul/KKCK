from django.contrib import admin
from .models import CustomUser  # Importa tu modelo de usuario personalizado

# Register your models here
admin.site.register(CustomUser)
