from rest_framework import serializers
from api.models import Company, Employee

# serializers is a module

# create serializers here


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # we can make a meta class and tells that which model is used.
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
    # with the help of these field which fields should be used that is passed
        fields="__all__"
    # we can add the fields include or exclude or seriaze the data


class EmployeeSerializer(serializers.HyperlinkedModelSerializer): #model serializer
    id = serializers.ReadOnlyField()
    class Meta: #meta means data about some data
        model = Employee
        fields="__all__"