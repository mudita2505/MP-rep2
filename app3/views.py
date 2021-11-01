from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions,viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import Diseaseserializer, UserSerializer, RegisterSerializer, Symptomserializer,Questionserializer, Treatmentserializer, Dietserializer
from app3.models import Disease, Symptom,Question,Option,Treatment,Diet,Disease
from rest_framework.decorators import api_view

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
        return user

class Symptomviewset(viewsets.ModelViewSet):
    queryset=Symptom.objects.all()
    serializer_class=Symptomserializer
 

@api_view(['GET'])
def get_questions(request):
   symptom = request.query_params.get('symptom', None)

   queryset = Question.objects.all()

   if symptom:
        try:
            symp = Symptom.objects.get(symptom=symptom)
        except:
            return Response({"error": "Symptom not found!"})
   
        queryset = queryset.filter(symp=symp)

   serializer = Questionserializer(queryset, many=True)
   return Response(serializer.data)


# @api_view(['GET'])
# def get_options(request):
#    option = request.query_params.get('options', None)

#    queryset = Option.objects.all()

#    if option:
#         try:
#             opt = Option.objects.get(option=option)
#         except:
#             return Response({"error": "Options not found!"})
   
#         queryset = queryset.filter(opt=opt)

#    serializer = Optionserializer(queryset, many=True)
#    return Response(serializer.data)

@api_view(['GET'])
def get_diseases(request):
   # symptom = request.query_params.get('symptom', None)

    # symptoms = request.body.get("symptoms", None)
    symptoms = request.query_params.get("symptoms")

    if (symptoms):
        # Expect ", " seperated list of symptom names
        symptoms = symptoms.split(',')

        result = {}

        for symptom_name in symptoms:
            try:
                symp = Symptom.objects.get(symptom=symptom_name)
            except:
                # Return error for invalid symptom name
                return Response({"error": f"Symptom not found!: {symptom_name}"})

            queryset = symp.disease_set.all()

            result[symptom_name] = [obj.disease for obj in queryset]
        
        return Response(result)
        
    else:
        # Return empty list when symptoms are not given
        return Response({})
        


#    queryset = Disease.objects.all()

#    if symptom:
#         try:
#             symp = Symptom.objects.get(symptom=symptom)
#         except:
#             return Response({"error": "Symptom not found!"})
   
#         queryset = symp.disease_set.all()

#    # serializer = Diseaseserializer(queryset, many=True)
#    # return Response(serializer.data)
#    return Response({ "diseases": [obj.disease for obj in queryset] })


@api_view(['GET'])
def get_treatment(request):
   disease = request.query_params.get('disease', None)

   queryset =Treatment.objects.all()

   if disease:
        try:
            diseases = Disease.objects.get(disease=disease)
        except:
            return Response({"error": "Disease not found!"})
   
        queryset = queryset.filter(treat=diseases)

   serializer = Treatmentserializer(queryset, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def get_diet(request):
   disease = request.query_params.get('disease', None)

   queryset = Diet.objects.all()

   if disease:
        try:
            diets = Disease.objects.get(disease=disease)
        except:
            return Response({"error": "Treatment not found!"})
   
        queryset = queryset.filter(diet=diets)

   serializer = Dietserializer(queryset, many=True)
   return Response(serializer.data)
