from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

def index(request):
    product_objects = Products.objects.all()

    #search code
    item_value = request.GET.get('item_value')
    if item_value != '' and item_value is not None:
        product_objects = product_objects.filter(title__icontains=item_value)

    
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

# Create your views here.
    return render(request,'index.html',{"product_objects":product_objects})


def detail(request,id):
    product_object= Products.objects.get(id=id)
    return render(request,'detail.html',{"product_object":product_object})


def test(request):
    product_object= Products.objects.all()
    return render(request,'test.html',{"product_object":product_object})

def checkout(request):
    return render(request,'checkout.html')