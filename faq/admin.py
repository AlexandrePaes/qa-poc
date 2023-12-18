from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_per_page = 1
    list_display = ('question', 'answer')
    list_editable = ('question', 'answer')
    list_display_links = None