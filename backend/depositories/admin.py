from django.contrib import admin
from .models import BookDepository
from import_export.admin import ImportExportActionModelAdmin


class BookDepositoryInline(admin.TabularInline):
    model = BookDepository
    extra = 0


class DepositoryAdmin(ImportExportActionModelAdmin):
    inlines = [BookDepositoryInline]

