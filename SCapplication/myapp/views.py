from django.shortcuts import render,redirect
import requests , secrets
from django.http import HttpResponse 
from django.views import View


def home(request):
    A=requests.get("http://127.0.0.1:8000/home").json()
    return render(request,'mytem/home.html',{'Course':A})

def about(request):
    return render(request,'mytem/about.html')

def course(request):
    A=requests.get("http://127.0.0.1:8000/home").json()
    return render(request,'mytem/course.html',{'Course':A})

def contact(request):
   if request.method == 'POST':
       data={"name":request.POST['name'],"email":request.POST['email'],"mobile":request.POST['mobile'],"message":request.POST['message']}
       response = requests.post("http://127.0.0.1:8000/Inquerry",data=data)
       asd=response.json()
       return render(request,"mytem/contact.html",{'key':asd})
   return render(request,'mytem/contact.html')

def oncourse(request,id):
    response = requests.get(f"http://127.0.0.1:8000/course/{id}").json() 
    return render(request,'mytem/oncourse.html',{'res':response})
    
def login(request):
  if request.method =='POST':
    data={"email":request.POST['email'],"password":request.POST['password']}
    if data != None:
       response=requests.post("http://127.0.0.1:8000/login",data=data).json()
       a=''
       for i in response.keys():
          a=i         
       if (a=="Success"):
          response="Log In SuccessFull"
          request.session['logged']=request.POST['email']
       elif (a=="Error"):
          response="Unauthenticate User Please Try Again"
    return render(request,"mytem/home.html",{'logg':response})
  if request.session.has_key('logged'):
     return redirect('/')
  return render(request,'mytem/login.html')

def register(request):
   if request.method =='POST':
      data= {"name":request.POST['name'],"mobile":request.POST['mobile'],"email":request.POST['email'],"otp":1,"password":request.POST['password']}
      response=requests.post('http://127.0.0.1:8000/register',data=data).json()
      return render(request,'mytem/verification.html')
   return render(request,'mytem/register.html')

def privacy(request):
   if request.session.has_key('logged'):
    return render(request,"mytem/privacy.html")
   return HttpResponse("hii pease login")

def Faqs(request):
    return render(request,"mytem/Faqs.html")

def terms(request):
    return render(request,"mytem/terms.html")

def logout(request):
   del request.session['logged']
   return redirect("/")

def Verify(request):
  if request.method =='POST':
    otp = request.POST.getlist('ottp')
    s=''
    s=s.join(otp)
    data={"name":s}
    response=requests.put("http://127.0.0.1:8000/register",data=data)
    return render(request,"mytem/home.html",{'res':s})
  return render(request,"mytem/verification.html")

class payment(View):
   def get(self,request,id):
    if request.session.has_key('logged'):
      response=requests.get(f"http://127.0.0.1:8000/course/{id}").json()
      return render(request,"mytem/payment.html",{'course':response})
    return redirect("login_game")
   def post(self,request,id):
     try:
         if request.session.has_key('logged'):
            data={"name":request.POST['name'],"email":request.POST['email'],"contact":request.POST['contact'],"Course_name":request.POST['Course_name']}
            key=secrets.token_hex(16)
            request.session['Payed']=key
            response=requests.post("http://127.0.0.1:8000/payment/",data=data).json()
            print(response)
            context={'payment':response}
            return render(request,"mytem/home.html",{"keyofpay":f"{data['Course_name']}"})
     except Exception as e:
         print(e)
         return render(request,"mytem/ServerError.html")
      # return redirect('login_game')
     

def course_Content(request):
  if 'Payed' in request.session:
      if request.session.has_key("logged") and request.session.has_key("Payed"):
         return HttpResponse("done")
      return HttpResponse('not have both')
  return redirect('/')
