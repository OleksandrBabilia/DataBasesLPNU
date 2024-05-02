from import_export.admin import ImportExportActionModelAdmin
from .models import Publisher

class PublisherAdmin(ImportExportActionModelAdmin):
    list_display = ["name", "address", "phone"] 
    list_filter = ["name", "address", "phone"] 
    # list_select_related = ["book_title"]
    
    def get_queryset(self, request):
        user = request.user
        if user.is_superuser: 
            return Publisher.objects.using('default').all()
        elif user.groups.filter(name='Manager').exists():
            return Publisher.objects.using('manager').all()
        else:
            return Publisher.objects.using('consultant').all()

