from django.shortcuts import render
from django.http import HttpResponse
from .models import Srinu
from srinu1.form import SrinuForm,EmpForm
from srinu1.functions import handle_uploaded_file

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello going to build Srinu app</h1>")
 
def srinu_list(request):
    srinu_obj = Srinu.objects.all()
    return render(request,'srinu_list.html',{'srinu_objects':srinu_obj})

def index(request):
    return render(request,'index.html')

def srinuform(request):
    sri = SrinuForm()
    return render(request,"sri_form.html",{'form':sri})

def empform(request):
    if request.method == "POST":
        emp = EmpForm(request.POST,request.FILES)
        if emp.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("file Uploaded Successfully")
    else:
        emp = EmpForm()
        return render(request,"emp_form.html",{"form":emp})