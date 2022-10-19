from django.contrib import admin

from applicant.models import User as UserModel


# Register your models here.
class User(admin.ModelAdmin):
    list_display = ('id', 'username')

admin.site.register(UserModel, User)