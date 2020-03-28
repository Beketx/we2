from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from api.models import*
# Create your views here.
def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return JsonResponse(product.to_json(),safe=False)
def categories_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)
def category_detail(request, category_id):
    category = Category.objects.get(id = category_id)
    return JsonResponse(category.to_json(), safe=False)
def products_by_category(request,fk):
    try:
        category = Category.objects.get(id = fk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    products = category.product_set.all()
    response = [product.to_json() for product in products]
    return JsonResponse(response, safe=False)