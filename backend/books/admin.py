from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportActionModelAdmin


class BookAdmin(ImportExportActionModelAdmin):
    list_display = ["title", "isbn", "publication_date", "price", "image_tag"]
    # list_select_related = ["author__first_name", "author__last_name", "publisher__name"]
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:80px"/>'.format(obj.cover.url))

