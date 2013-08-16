from django.contrib import admin
from pockettracker.models import pocketdata

class PocketAdmin(admin.ModelAdmin):
  list_display = ['item', 'category']
  list_filter = ['date']
  search_fields = ['item', 'date']
  date_hierarchy = 'date'
  save_on_top = True
  prepopulated_fields = {"comment":("item",)}

admin.site.register(pocketdata, PocketAdmin)
