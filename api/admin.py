from django.contrib import admin
from .models import KerogenModel

# Register your models here.


class KerogenModelAdmin(admin.ModelAdmin):
    # 允许所有人查看，不进行权限控制
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(KerogenModel, KerogenModelAdmin)
