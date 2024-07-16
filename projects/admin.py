from django.contrib import admin
from . models import Category, Contributor, Project, ProjectImages, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Contributor)
admin.site.register(ProjectImages)
admin.site.register(Project)
admin.site.register(Tag)