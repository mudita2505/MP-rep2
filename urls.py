from django import urls
from django.db import router
from rest_framework import views,routers
from app3.views import RegisterAPI,LoginAPI, get_diet, get_diseases, get_diseases,get_questions,Symptomviewset, get_treatment
from django.urls import include,path
from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r'symptom', Symptomviewset)



urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('question/',get_questions),
    # path('option/',get_options),
    path('disease/',get_diseases),
    path('treatment/',get_treatment),
    path('diet/',get_diet),
    path('', include(router.urls)),
]
