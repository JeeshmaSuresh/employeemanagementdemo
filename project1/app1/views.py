from django.shortcuts import render,redirect
from django.views import View
from app1.models import employee

# Create your views here.
class Home(View):
    def get(self,request):
        emp=employee.objects.all()
        return render(request,'index.html',{"employee":emp})
    
class registerview(View):
    def get(self,request):
        return render(request,'register.html')
        
    def post(self,request):
        emp_name=request.POST.get("name")
        salary=request.POST.get("salary")
        phone=request.POST.get("phone")
        designation=request.POST.get("designation")
        employee.objects.create(emp_name=emp_name,salary=salary,phone=phone,designation=designation)
        return redirect('home_view')
        
class employeeview(View):
    def get(self,request,args,*kwargs):
        id=kwargs.get("id")
        emp=employee.objects.get(id=id)
        return render(request,"detail.html",{"emp":emp}) 

class employeeEditView(View):
    def get(self,request,args,*kwargs):
        id=kwargs.get("id")
        emp=employee.objects.get(id=id)
        return render(request,"edit.html",{"emp":emp})

def post(self,request,args,*kwargs):
        name=request.POST.get("name")
        salary=request.POST.get("salary")
        phone=request.POST.get("phone")
        desig=request.POST.get("designation")
        empid=kwargs.get("id")
        emp=employee.objects.get(id=empid)
        emp.emp_name=name 
        emp.salary=salary 
        emp.phone=phone
        emp.designation=desig
        emp.save()
        return redirect('home_view') 

class employeeDelete(View):
    def get(self,request,args,*kwargs):
        id=kwargs.get("id")
        emp=employee.objects.get(id=id)
        emp.delete()
        return redirect('home_view')

