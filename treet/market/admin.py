from django.contrib import admin

from market.models import Treet

class TreetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(Treet, TreetAdmin)
