from django.contrib import admin

from main.models import Student, Subject
from materials.models import Materials


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "is_activ",
    )
    list_filter = ("is_activ",)
    search_fields = (
        "first_name",
        "last_name",
    )


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body"
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student',)
    list_filter = ('student',)
