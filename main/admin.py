from django.contrib import admin
from main.models import Student

# """Вывод студентов"""
# admin.site.register(Student)

"""Вывод списка студентов"""


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)
