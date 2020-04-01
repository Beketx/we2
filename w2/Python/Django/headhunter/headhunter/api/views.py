from django.shortcuts import render
from api.models import Company,Vacancy
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
# Create your views here.

def companies_list(request):
    companies = Company.objects.all()
    company_json = [company.to_json() for company in companies]
    return JsonResponse(company_json, safe=False)

def companies_detail_by_id(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(company.to_json())

def companies_detail_by_name(request,company_name):
    try:
        company = Company.objects.get(name=company_name)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(company.to_json())

def vacancies_of_company(request,company_name):
    try:
        kompany = Company.objects.get(name=company_name)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    vac_com = kompany.vacancy_set.all()
    vac_com_json = [vac.to_json() for vac in vac_com]
    return JsonResponse(vac_com_json, safe=False)

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vac.to_json() for vac in vacancies]
    return JsonResponse(vacancies_json, safe=False)
def vacancies_detail(request,vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse(vacancy.to_json(),safe=False)
def vacancies_top_ten(request):
    vacancies = Vacancy.objects.all()
    top_ten = vacancies.order_by('-salary')
    top_ten_json = [top.to_json() for top in top_ten]
    return JsonResponse(top_ten_json,safe=False)