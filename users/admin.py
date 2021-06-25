from django.contrib import admin
from users.models import User
from baskets.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    ordering = ('username',)
    search_fields = ('username',)
    inlines = (BasketAdmin,)
