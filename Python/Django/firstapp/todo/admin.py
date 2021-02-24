from django.contrib import admin
from . import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


# Register your models here.
admin.site.register(Todo, TodoAdmin)


