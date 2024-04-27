from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birthdate", "nationality"]
    list_select_related = ["Book__title"]
