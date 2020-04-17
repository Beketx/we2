from django.urls import path
from api.views import *
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('login/',obtain_jwt_token),
    path('companies/',companies_list),
    path('companies/<int:id>/',companies_detail_by_id),
    path('companies/<str:company_name>/',companies_detail_by_name),
    path('companies/<str:company_name>/vacancies/',vacancies_of_company),
    path('vacancies/',VacancyViewSet.as_view()),
    path('vacancies/<int:pk>/',SingleVacancyViewSet.as_view()),
    path('vacancies/top_ten/',vacancies_top_ten)
] 