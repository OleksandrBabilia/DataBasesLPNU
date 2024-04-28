from import_export.admin import ImportExportActionModelAdmin


class AuthorAdmin(ImportExportActionModelAdmin):
    list_display = ["first_name", "last_name", "birthdate", "nationality"]
    list_filter = ["first_name", "last_name", "birthdate", "nationality"]
    # list_select_related = ["Book__title"]

