from django.shortcuts import render
from .models import Proveedor

# Create your views here.
def MostrarProveedor(request):
    """
    lista a los proveedor
    """
    proveedores= Proveedor.objects.all()
    context={"proveedores":proveedores}
    return render(request,'listProveedor.html',context)
