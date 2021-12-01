from django.contrib import admin

# Register your models here.
from .models import Student, Grade_Level

# Register your models here.
admin.site.register(Student)
admin.site.register(Grade_Level)