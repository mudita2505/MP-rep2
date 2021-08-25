from django.shortcuts import render
from .forms import Userregistration
# Create your views here.
def showdata(request):

    if request.method=='POST':
        obj=Userregistration(request.POST)
        obj=Userregistration()
        
        if (obj.is_valid()):
            print(obj.cleaned_data['name'])
            print(obj.cleaned_data['email'])
            print(obj.cleaned_data['password'])

        print("From Post request!")
    
    else:
        obj = Userregistration()
        print("From get request!")

    return render(request,'formapp/registration.html',{'form':obj})
    