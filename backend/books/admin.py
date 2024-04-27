from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "isbn", "publication_date", "price"]
    list_select_related = ["author__first_name", "author__last_name", "publisher__name"]
