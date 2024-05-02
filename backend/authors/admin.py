from import_export.admin import ImportExportActionModelAdmin
from .models import Author

class AuthorAdmin(ImportExportActionModelAdmin):
    list_display = ["first_name", "last_name", "birthdate", "nationality"]
    list_filter = ["first_name", "last_name", "birthdate", "nationality"]
    # list_select_related = ["Book__title"]
    
    def get_queryset(self, request):
        user = request.user
        if user.is_superuser: 
            return Author.objects.using('default').all()
        elif user.groups.filter(name='Manager').exists():
            return Author.objects.using('manager').all()
        else:
            return Author.objects.using('consultant').all()


