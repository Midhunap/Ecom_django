from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #Django uses UserAdmin to render the nice admin look for User model. By just using this in our admin.py-file, we can get the same look for our model.
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active') #Contain only fields in your `custom-user-model`
    # search_fields = ()  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ('-date_joined',)  # Contain only fields in your `custom-user-model` intended to ordering ,-date_joined shows the decending order
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')

    filter_horizontal = () # Leave it empty. You have neither `groups` or `user_permissions`
    list_filter = ()  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    fieldsets = ()
admin.site.register(Account,AccountAdmin)