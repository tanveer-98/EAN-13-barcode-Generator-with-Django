from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    context={}

    if request.method == 'POST':
        data = request.POST
        newproduct = Product()
        newproduct.name = data['name']
        newproduct.countryid = data['countryid']
        newproduct.manufacturercode = data['manufacturercode']
        newproduct.productcode = data['productcode']
        newproduct.save()
        
        context = {'name':data['name']}
        return render(request,'index.html',context)
    return render(request,'index.html',context)
