from django.contrib import admin
from . import models

admin.site.register(models.BaseToken)
admin.site.register(models.Metadata)

# Register your models here.
