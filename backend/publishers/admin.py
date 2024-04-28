from import_export.admin import ImportExportActionModelAdmin


class PublisherAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "address", "phone"] 
    list_filter = ["name", "address", "phone"] 
    # list_select_related = ["book_title"]

