from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)# used for registration identifications
admin.site.register(Person)# helps  in completing all the required fields in all documents
admin.site.register(Province)
admin.site.register(Commune)
admin.site.register(Zone)
admin.site.register(Quarter)
admin.site.register(IdentiteComplete)