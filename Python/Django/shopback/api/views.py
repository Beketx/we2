from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.

def product_list(request):
    return HttpResponse('Products')
def product_detail(request, product_id):
    return HttpResponse(f'product_id:{product_id}')
def category_list(request):
    return HttpResponse('Categories')
def 