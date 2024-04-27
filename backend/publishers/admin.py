from django.contrib import admin


class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name", "adress", "phone"] 
    list_select_related = ["book_title"]

