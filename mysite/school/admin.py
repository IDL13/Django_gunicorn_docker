from django.contrib import admin
from .models import *

# class CastomerAdmin(admin.ModelAdmin):
#     list_display = ('login', 'password')

# class AdressAdmin(admin.ModelAdmin):
#     list_display = ('id','adress',)
#     search_fields = ('adress',)

class AccountingAdmin(admin.ModelAdmin):
    list_display = ('users', 'technincs', 'create', 'tecNumber',)
    search_fields = ('users', 'technincs', 'tecNumber',)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('technincs', 'tecNumber',)
    search_fields = ('tecNumber',)

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
    search_field = ('titles','files')
    
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id','jobtitle',)    

# admin.site.register(Adress, AdressAdmin)
admin.site.register(Accounting, AccountingAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(File, FileAdmin)
# admin.site.register(User,UserAdmin)
# admin.site.register(Castomer, CastomerAdmin)