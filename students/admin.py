from django.contrib import admin

from .models import Student, Department


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_no", "gender", "dob", "address"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["department_name"]
