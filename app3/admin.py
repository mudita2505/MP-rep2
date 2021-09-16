from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app3.models import Question,Symptom,Option
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