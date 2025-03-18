from django.contrib import admin
from account.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'username', 'first_name', 'last_name')
    search_fields = ('username','first_name', 'last_name',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')


