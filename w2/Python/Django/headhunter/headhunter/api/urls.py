from django.urls import path
from api.views import *
urlpatterns = [
    path('companies/',companies_list),
    path('companies/<int:company_id>/',companies_detail_by_id),
    path('companies/<str:company_name>/',companies_detail_by_name),
    path('companies/<str:company_name>/vacancies/',vacancies_of_company),
    path('vacancies/',vacancies_list),
    path('vacancies/<int:vacancy_id>/',vacancies_detail),
    path('vacancies/top_ten/',vacancies_top_ten)
]