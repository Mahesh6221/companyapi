from django.contrib import admin
from api.models import Company,Employee


class CompanyAdmin(admin.ModelAdmin):
    # extends admin.ModelAdmin
    list_display=('name','location','type')
    # to search a company
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    # extends admin.ModelAdmin
    list_display=('name','email','company')
    # filter employee using company
    list_filter=('company',)


# Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

