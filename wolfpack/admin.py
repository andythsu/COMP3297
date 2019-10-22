from django.contrib import admin
from .models import ProductOwner,ScrumMaster,Developer,Project,PBI


admin.site.register(ProductOwner)
admin.site.register(ScrumMaster)
admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(PBI)
# Register your models here.
