from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app3.models import  Diet, Question,Symptom,Option,Disease, Treatment
# Register your models here.
@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display=['symptom']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['question','symp']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display=['options','opt']

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display=['disease']

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display=['treatment','treat']

@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display=['diet_to_follow','diet']