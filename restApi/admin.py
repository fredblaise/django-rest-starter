from django.contrib import admin
from .models import Portfolio, Project

# Register your models here.


@admin.register(Portfolio)
class ModelAdmin(admin.ModelAdmin):
    list_display = Portfolio.DisplayFields


@admin.register(Project)
class ModelAdmin(admin.ModelAdmin):
    list_display = Project.DisplayFields
