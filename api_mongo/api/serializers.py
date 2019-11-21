from rest_framework import serializers
from . import models

# class UserSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = models.User
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'
        # fields = ['comp_id', 'comp_name', 'address', 'tel']