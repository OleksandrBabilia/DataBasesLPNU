"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from authors.admin import AuthorAdmin 
from authors.models import Author 
from authors.viewsets import AuthorViewSet

from publishers.models import Publisher
from publishers.admin import PublisherAdmin
from publishers.viewsets import PublisherViewSet

from books.models import Book
from books.admin import BookAdmin
from books.viewsets import BookViewSet

from depositories.models import Depository
from depositories.admin import DepositoryAdmin

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Depository, DepositoryAdmin)

schema_view = get_schema_view(
    openapi.Info(
        title="Book Depository API ",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_title = "Book Depository Admin"
admin.site.site_header = "Book Depository Administration"
admin.site.index_title = "Site Admin"

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)), 
    path('admin/', admin.site.urls),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

