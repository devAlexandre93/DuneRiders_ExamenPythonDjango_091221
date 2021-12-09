from django.contrib import admin

from persona_app.models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['first_name__startswith', 'last_name__startswith', 'id__startswith']

admin.site.register(Persona, PersonaAdmin)
