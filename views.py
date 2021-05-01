


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#import datetime.timedelta
import datetime
#viw function first shold be req only
from django.template import Template,Context
from django.template.loader import get_template
from my_app.models import formcontact

def index(request):
    return HttpResponse('Hello world')
def welcome(request):
    return HttpResponse('welcome to django')
def current(request):
    now=datetime.datetime.now()
    html="<html><body>now %s</body></html>"%now
    return HttpResponse(html)
def name(request):
    name=input()
    html="<html><body><B>Hello %s</B></body></html>"%name 
    return HttpResponse(html)
def onehourahed(request):
    dt1=datetime.datetime.now()+datetime.timedelta(hours=1)
    html="<html><body><i>In %s hours  (s) it will be %s <i></body></html>" %(1,dt1)
    return HttpResponse(html)
def add(request):
    num1=int(input())
    num2=int(input())
    ans=num1+num2
    html="<html><body> %s </body></html>" %ans
    return HttpResponse(html)
def addd(request):
    print('enter name \n')
    num1=int(input())
    num2=int(input())
    ans=num1+num2
    sdi={"res":ans}
    return render(request, "add.html", sdi)
def hours_add(request,offset):
    try:
       offset=int(offset)
    except ValueError:
       raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body> time  affter %s  will be  %s </body></html>" %(offset,dt)
    return HttpResponse(html)
    
def stati(request):
    return render(request,"webpage.html")
def sample(request): 
    return render(request,"label0.html")
def res(request):
    val1=request.GET['fname']
    val2=request.GET['lname']
    val3=request.GET['email']
    
    return render(request,"result.html",{'name':val1,'lname':val2,'email':val3})
def det(request):
    return render(request,"getdet.html")
    
def details(request):
    now = datetime.datetime.now()
    val1=request.GET['fname']
    val2=request.GET['phone']
    val3=request.GET['intrest']
    val4=request.GET['email']
    val5=request.GET['dept']
    val6=request.GET['city']
 
    t=get_template("final.html")
    c=Context({"name":val1,"contactno":val2,"intrest":val3,"cgpa":val4,"date":now,"branch":val5,"city":val6})
    con=c.flatten()
    html=t.render(con)
    return HttpResponse(html)

def ss(request):
    
    name=request.GET['name']
    email=request.GET['email']
    ins=formcontact(name=name,email=email)
    ins.save()
    html="<html><body> Added {{name}}</body></html>"
    print('Data added')
    return render(request,"new.html")
    #return HttpResponse(html)

def form3(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		phone=request.POST['phone']
	values = request.POST
	print("values are..............", values)
	for k in values.keys():
		print("Key is" + k)
	for v in values.values():
		print("Values is" + v)
	return HttpResponse(" successfully printed  %s   values" % values.items())
#	return render(request, 'home.html')
###########################################################################################################
def days_add(request,offset):
    try:
       offset=int(offset)
    except ValueError:
       raise Http404()
    EndDate = datetime.datetime.today()+datetime.timedelta(days=offset)
    html="<html><body><H1><i> Date After %s days will be  %s .</i><H1> </body></html>" %(offset,EndDate)
    return HttpResponse(html)

def dob(request): 
    birth_year = int(input("Enter your year of birth: \n"))
    birth_month = int(input("Enter your month of birth: \n"))
    birth_day = int(input("Enter your day of birth: \n"))
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day
    age_year = current_year - birth_year
    age_month = abs(current_month-birth_month)
    age_day = abs(current_day-birth_day)
    html="<html><body> Age is %s </body></html>" %age_year
    #return HttpResponse(html)
    return render(request,"age.html",{'year':age_year,'month':age_month,'days':age_day})


  
    
 
    
    
   
   
    
    
