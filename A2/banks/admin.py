from django.contrib import admin
from .models import BankModel, BranchModel
# Register your models here.
@admin.register(BankModel)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id','owner', 'bankname', 'swift_code', 'inst_num', 'description']


@admin.register(BranchModel)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','bank','name', 'transit_num', 'address', 'email', 'capacity']
