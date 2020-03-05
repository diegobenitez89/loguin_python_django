from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado, Producto


class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timestamp"]
    form = RegModelForm
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fiellds = ["email","nombre"]


    #class Meta:
    #    model = Registrado
admin.site.register(Registrado,AdminRegistrado)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","stock"]
    search_fields = ["nombre"] 
    list_per_page = 10




admin.site.register(Producto,ProductoAdmin)
