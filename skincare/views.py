from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'skincare/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        
        Product.objects.create(
            name=name,
            category=category,
            description=description
        )
        return redirect('product_list')
    
    return render(request, 'skincare/product_form.html')

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'skincare/product_confirm_delete.html', {'product': product})

# Create your views here.
