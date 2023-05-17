from django.contrib import admin

# Register your models here.
from django101.web.models import Todo, Category


@admin.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass