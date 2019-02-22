from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Reg,Event,Querry
from .forms import LoginForm,RegForm,EventForm,QuerryForm

def home(request):
    if request.method=='POST':
        qform=QuerryForm(request.POST)
        if qform.is_valid():
            mobile_no=request.POST.get('mobile_no','')
            query=request.POST.get('querry','')
            qry=Querry(mobile_no=mobile_no,query=query)
            qry.save()
            return redirect('./')
    else:
        qform=QuerryForm()
        return render(request,'home.html',{'form3':qform})
def reg(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            course=request.POST.get('course','')
            college=request.POST.get('college','')
            email=request.POST.get('email','')
            contact_no=request.POST.get('contact_no','')
            password=request.POST.get('password','')
            reg=Reg(name=name,course=course,college=college,email=email,contact_no=contact_no,password=password)
            reg.save()
            return redirect('./login')
    else:
        form=RegForm()
        return render(request,'register.html',{'form':form})
def login(request):
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            email=MyLoginForm.cleaned_data['email']
            password=MyLoginForm.cleaned_data['password']
            dbemail = Reg.objects.filter(email=email)
            dbpwd = Reg.objects.filter(password=password)
            if not dbemail or dbpwd:
                return redirect('./event')
            else:
                return redirect('./login')
        else:
            print(MyLoginForm.errors)
    else:
        form1=LoginForm()
        return render(request,'login.html',{'form1':form1})
def event(request):
    if request.method=="POST":
        MyForm = EventForm(request.POST)
        if MyForm.is_valid():
            participant=request.POST.get('participant','')
            event=request.POST.get('event','')
            eve=Event(participant=participant,event=event)
            eve.save()
            return redirect('./event')
    else:
        MyForm=EventForm()
        return render(request,'event.html',{'form2':MyForm})
