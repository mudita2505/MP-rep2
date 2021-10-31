from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from app3.models import Symptom, Question, Option, Disease
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name' ,'email', 'password')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class Symptomserializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ('symptom',)

class Questionserializer(serializers.ModelSerializer):
    symptom = serializers.CharField(source='symp')
    ques = serializers.CharField(source='question')
    optio = serializers.StringRelatedField(many=True,source='options')
    class Meta:
        model = Question
        fields = ('symptom','ques','optio')

# class Optionserializer(serializers.ModelSerializer):
#     ques = serializers.CharField(source='question')
#     option = serializers.StringRelatedField(many=True,source='options')
#     class Meta:
#         model = Option
#         fields =('opt','optio')

class Diseaseserializer(serializers.ModelSerializer):
    symptom = serializers.CharField(source='symp')
    class Meta:
        model = Disease
        fields = ('symptom','disease')
    

