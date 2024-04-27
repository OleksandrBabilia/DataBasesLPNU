from django.contrib import admin


class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone"] 
    list_select_related = ["book_title"]

