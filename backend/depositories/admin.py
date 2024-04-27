from django.contrib import admin
from .models import Depository, BookDepository


class BookDepositoryInline(admin.TabularInline):
    model = BookDepository
    extra = 0


class DepositoryAdmin(admin.ModelAdmin):
    inlines = [BookDepositoryInline]

