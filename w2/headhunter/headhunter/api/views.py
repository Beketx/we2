from django.shortcuts import render
from api.models import Company,Vacancy
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from rest_framework.views import APIView
from .serializers import CompanySerializer, VacancySerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView
# Create your views here.
@api_view(['GET','POST'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status = 204)
    elif request.method == 'POST':
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            saved_company = serializer.save()
        return Response(serializer.data)
        # company_json = [company.to_json() for company in companies]
        # return JsonResponse(company_json, safe=False)
@api_view(['GET','PUT','DELETE'])
def companies_detail_by_id(request,id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist as e:
            return Response({"error":str(e)})
    elif request.method == 'PUT':
        data = request.data
        company = get_object_or_404(Company, id=id)
        serializer = CompanySerializer(instance=company,data=data)
        if serializer.is_valid():
            saved_company = serializer.save()
            return Response(serializer.data, status = 200)
        return Response({"error":serializer.errors})
    elif request.method == 'DELETE':
        company = get_object_or_404(Company,id=id)
        company.delete()
        return Response({"deleted":"company {} successfully deleted "}.format(company.name))
            # try:
            #     company = Company.objects.get(id=company_id)
            # except Company.DoesNotExist as e:
            #     return JsonResponse({'error':str(e)})
            # return JsonResponse(company.to_json())


def companies_detail_by_name(request,company_name):
    if request.method == 'GET':
        if company_name != 'create':
            company = Company.objects.get(name=company_name)
            # company = get_object_or_404(Company, name = company_name)
            serializer = CompanySerializer(company)
            return Response(serializer.data)

        # try:
        #     company = Company.objects.get(name=company_name)
        # except Company.DoesNotExist as e:
        #     return JsonResponse({'error':str(e)})
        # return JsonResponse(company.to_json())

def vacancies_of_company(request,company_name):
    if request.method == 'GET':
        try:
            kompany = Company.objects.get(name=company_name)
        except Company.DoesNotExist as e:
            return JsonResponse({'error':str(e)})
        vac_com = kompany.vacancy_set.all()
        vac_com_json = [vac.to_json() for vac in vac_com]
        return JsonResponse(vac_com_json, safe=False)

class VacancyViewSet(ListCreateAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    permission_classes = [IsAuthenticated]
    # def perform_create(self,serializer):
    #     vacancy = get_object_or_404(Vacancy, id = self.request.data.get('id'))
    #     return serializer.save(vacancy=vacancy)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)




    # def vacancies_list(request):
    #     vacancies = Vacancy.objects.all()
    #     vacancies_json = [vac.to_json() for vac in vacancies]
    #     return JsonResponse(vacancies_json, safe=False)
    # def vacancies_detail(request,vacancy_id):
    #     try:
    #         vacancy = Vacancy.objects.get(id=vacancy_id)
    #     except Vacancy.DoesNotExist as e:
    #         return JsonResponse({'error':str(e)})

    #     return JsonResponse(vacancy.to_json(),safe=False)
class SingleVacancyViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


def vacancies_top_ten(request):
    vacancies = Vacancy.objects.all()
    top_ten = vacancies.order_by('-salary')
    top_ten_json = [top.to_json() for top in top_ten]
    return JsonResponse(top_ten_json,safe=False)