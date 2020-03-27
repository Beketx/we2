from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product
from api.models import Category
# import json
# Create your views here.
# products = [{
#     'id': 1,
#     'name':f'product - {1}',
#     'price':1*1000,
#     'category': 'luxury'
# },{
#     'id': 2,
#     'name':f'product - {2}',
#     'price':2*1000,
#     'category': 'simple'
# },
# {
#     'id': 3,
#     'name':f'product - {3}',
#     'price':3*1000,
#     'category': 'luxury'
# },
# {
#     'id': 4,
#     'name':f'product - {4}',
#     'price':4*1000,
#     'category': 'simple'
# },
# {
#     'id': 5,
#     'name':f'product - {5}',
#     'price':5*1000,
#     'category': 'luxury'
# },
# {
#     'id': 6,
#     'name':f'product - {6}',
#     'price':6*1000,
#     'category': 'simple'
# },

# {
#     'id': 7,
#     'name':f'product - {7}',
#     'price':7*1000,
#     'category': 'luxury'
# },

# {
#     'id': 8,
#     'name':f'product - {8}',
#     'price':8*1000,
#     'category': 'simple'
# },

# {
#     'id': 9,
#     'name':f'product - {9}',
#     'price':9*1000,
#     'category': 'luxury'
# },

# {
#     'id': 10,
#     'name':f'product - {10}',
#     'price':10*1000,
#     'category': 'simple'
# }]
# categories = [
#     {'name':'luxury'},
#     {'name':'simple'}
# ]
# products = [{
#     'name':f'product - {i}',
#     'price':i*1000
# }for i in range(1,5)]
# for i in range(1,5):
#     products.append(
#         {
#             'id': i,
#             'name':f'product - {i}',
#             'price':i*1000, 
#             'category': 'luxury'
#         }
#     )


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json()  for product in products]
    return JsonResponse(products_json, safe=False)

def product_detail(request, product_id):
    try: 
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())
    # product_json = [products_json() for product in products]
    # for product in products:  
    #     if product['id']==product_id:
    #         return JsonResponse(product)
    
    # return JsonResponse({'Error':'Product does not exist'})

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)
    
def category_detail(request, category_name):
    for category in categories:
        if category['name']==category_name:
            return JsonResponse(category, safe=False)
    return JsonResponse({'Error':'Category not found'})

def category_product(request, category_name, product):
    products = Product.objects.all()
    products_json = []
    for product in products:
        product = product.to_json()
        if(product['category']==category_id):
            products_json.append(product)
    return JsonResponse(products_json, safe=False)
