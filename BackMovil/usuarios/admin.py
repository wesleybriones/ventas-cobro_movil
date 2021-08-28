from django.contrib import admin
from usuarios.models import Vendedor, Cliente, Usuario, Producto, Empaque, Categoria, UnidadMedida, Rol
# Register your models here.


# class VendedorAdmin(admin.ModelAdmin):
#     list_display = ['numventas']

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(UnidadMedida)
admin.site.register(Rol)