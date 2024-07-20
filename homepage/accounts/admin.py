from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします
