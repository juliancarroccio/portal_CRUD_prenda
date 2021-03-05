from django.contrib import admin
from .models import Producto, Color, Familia, Industria, Marca, Proveedor, Talle


# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ['marca','proveedor','industria','color','talle','familia','codigo_barra','descripcion','precio', 'stock','iva']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display = ['descripcion_color']

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
	list_display = ['descripcion_familia']

@admin.register(Industria)
class IndustriaAdmin(admin.ModelAdmin):
	list_display = ['descripcion_industria']

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
	list_display = ['descripcion_marca']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ['descripcion_proveedor']

@admin.register(Talle)
class TalleAdmin(admin.ModelAdmin):
	list_display = ['descripcion_talle']
