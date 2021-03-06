from django.contrib import admin

from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model_name', 'organization', 'building')
    list_filter = ('organization', 'building', 'contact_1_name')


admin.site.register(Asset, AssetAdmin)
