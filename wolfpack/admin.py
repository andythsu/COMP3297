from django.contrib import admin
from .models import ProductOwner, ScrumMaster, Developer, Project, ProductBacklogItem, SprintBacklog, SprintTask


admin.site.register(ProductOwner)
admin.site.register(ScrumMaster)
admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(ProductBacklogItem)
admin.site.register(SprintBacklog)
admin.site.register(SprintTask)

# Register your models here.
