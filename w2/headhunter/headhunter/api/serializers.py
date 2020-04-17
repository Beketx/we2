from rest_framework import serializers
from api.models import Company,Vacancy
class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    city = serializers.CharField(max_length=30)
    address = serializers.CharField()

    def create(self,validated_data):
        company = Company.objects.create(name=validated_data.get('name'))
        return company
        
    def update(self,instance,validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.city = validated_data['city']
        instance.address = validated_data['address']
        instance.save()
        return instance
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['name','description','salary','company']
        # fields = '__all__'