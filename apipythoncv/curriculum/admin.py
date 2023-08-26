from django.contrib import admin
from .models import Stack, ProjectDev, EmploymentHistory, Academy, HobbiesExtras, Skills, Facts

# Register your models here.

admin.site.register(Stack)
admin.site.register(ProjectDev)
admin.site.register(EmploymentHistory)
admin.site.register(Academy)
admin.site.register(HobbiesExtras)
admin.site.register(Skills)
admin.site.register(Facts)