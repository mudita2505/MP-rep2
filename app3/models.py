from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class Symptom(models.Model):
    symptom=models.CharField(max_length=200)
    def __str__(self):
        return self.symptom

class Question(models.Model):
    symp=models.ForeignKey(Symptom,on_delete=CASCADE)
    question=models.CharField(max_length=500,default='none')
    def __str__(self):
        return self.question

class Option(models.Model):
    opt=models.ForeignKey(Question,on_delete=CASCADE,related_name='options')
    options=models.CharField(max_length=100,default='none')
    def __str__(self):
        return self.options
   
class Disease(models.Model):
    symp=models.ManyToManyField(Symptom)
    disease=models.CharField(max_length=300)
    def __str__(self):
        return self.disease
        