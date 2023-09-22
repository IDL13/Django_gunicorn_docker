from django.contrib import admin
from .models import *


class AccountingAdmin(admin.ModelAdmin):
    list_display = ('users', 'technincs', 'create', 'tecNumber',)
    search_fields = ('users', 'technincs', 'tecNumber',)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('technincs', 'tecNumber',)
    search_fields = ('tecNumber',)


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
    search_field = ('titles','files')
    
admin.site.register(Accounting, AccountingAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(File, FileAdmin)
