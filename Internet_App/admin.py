from django.contrib import admin
from .models import *
# Register your models here.    

class UserAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id','role','firstname','lastname','gmail','password','city','state','mobile')


admin.site.register(signupmaster,UserAdmin)
