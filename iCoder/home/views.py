from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    # return HttpResponse('This is home page')
    return render(request,'home/home.html')

def contact(request):
    # return HttpResponse('This is contact page')  
    # messages.error(request,'Welcome to contact')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        print(name,email,phone,content)

        if len(name)<2 or len(email)<7 or len(phone)<10 or len(content)<2:
            messages.error(request,"please fill up the form correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your message has been received successfully, we'll try to reach you soon")
    return render(request,'home/contact.html')

def about(request):
    # return HttpResponse('This is about page') 
    return render(request,'home/about.html')

def workout(request):
    return render(request,'home/workout.html')    

def endurance(request):
    return render(request,'home/endurance.html')     

def strength_training(request):
    return render(request,'home/strength_training.html')     

def cross_training(request):
    return render(request,'home/cross_training.html')     

def hitt(request):
    return render(request,'home/hitt.html')     

def core_strength(request):
    return render(request,'home/core_strength.html')     

def resistance(request):
    return render(request,'home/resistance.html')     

def handlesignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST.get('pass2')

        # Check for errorneous inputs

        if len(username)>10 or len(username)<3:
            messages.error(request,"User must be under 3-10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Username must be within alphanumeric characters")
            return redirect('home')

        if len(pass1)<8:
            messages.error(request,"Please create Strong password with alphanumeric character and min 8 characters")
            return redirect('home') 

        if pass1 != pass2:
            messages.error(request,"confirm your password again")   
            return redirect('home') 

        # Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        # myuser.passc=pass2
        myuser.save()
        messages.success(request,'Your Fitness Account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')    


def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        
        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,loginusername+', You are successfully logged in')
            return redirect('home')
        else:  
            messages.error(request,"Invalid credentials, please try again ")
            return redirect('home')  
    else:
        return HttpResponse('404 - Not Found')


    


def handlelogout(request):
    logout(request)
    messages.success(request,'You are successfully logged Out')
    return redirect('home')

    # return HttpResponse('Logouttttttttttt')    


def BMI(request):
    return render(request,'home/BMI.html')

def add(request):
    ht=float(request.GET['height'])
    wt=float(request.GET['weight'])

    res=round((wt/(ht*ht))*10000,2)

    return render(request,'home/BMIANS.html',{'result':res})     