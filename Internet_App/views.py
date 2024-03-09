from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from ISP_Project import settings
import random

from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from Internet_App.models import plan

status=False
def index(request):
    global status
    if request.method=='POST':
        

        unm=request.POST['gmail']
        pas=request.POST['password']
        r =request.POST['role']

        user=signupmaster.objects.filter(gmail=unm,password=pas, role=r)
        fnm_session = signupmaster.objects.get(gmail=unm)
        uid=signupmaster.objects.get(gmail=unm)
        c_role = uid.role
        print("UserID:",uid.id)
        print("Current role",c_role)

        if user:
            print("Login Successfully!")
            # request.session['user']=unm
            request.session['user']= fnm_session.firstname
            request.session['uid']=uid.id
            request.session['c_role']= c_role
            #msg="Login Successfully!"
            status=True
            return redirect('welcome')
        else:
            print("Error!Login Fail...Try again")
    return render(request,'index.html')

def customer_det(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data_det= signupmaster.objects.filter(role="Customer")
    return  render(request,"customer_det.html", {'c_role':c_role, 'user':user, 'data':data_det, 'id':id})

def welcome_page(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')

    return  render(request,"welcome.html", {'c_role':c_role, 'user':user}) 

def plans(request):
    user=request.session.get('user')
    # ufn = user.firstname
    # print(ufn)
    uid=request.session.get('uid')
    cuser=signupmaster.objects.get(id=uid)
    return render(request, 'plans.html',{'user':user,'cuser':cuser})


def complaint(request):
    user = request.session.get('user')
    c_role = request.session.get('c_role')
    data=complain.objects.all()
    # p_id = complaint.objects.get(id = id)
    # p_data = complaint.objects.all()
    if request.method=='POST':
        comp=complaint_form(request.POST, request.FILES)
        if comp.is_valid():
            comp.save()
            print("Your Complaint has been submitted!")
            # send mail
            sub="Complaint Submitted!"
            message = f"Hello {request.POST['name']}! \n\nYour Complaint is Submited!!! .\n\nIf any Queries, plz feel free to contact us...\nRegards \nHostit PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect("welcome")
        else:
            print(comp.errors)
            print("Sorry Try again")
    return render(request, 'complaint.html', {'c_role':c_role, 'user':user, 'data':data})

def status_update(request,id):
    stid = complain.objects.get(id = id)
    if request.method=='POST':
        data=complaint_update(request.POST,instance=stid)
        if data.is_valid(): #true
            data.save()
            print("Your data has been updated!")
            return redirect('complaint')
        else:
            print(data.errors)
    return render(request, 'status_update.html', {'stid':stid})

def buy_1099(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=signupmaster.objects.get(id=uid)
    if request.method == "POST":
        newplan = plan_form(request.POST, request.FILES)
        if newplan.is_valid():
            newplan.save()
            print("Plan saved")
            # send mail
            sub="Thank you"
            message = f"Hello {request.POST['fullname']}! \n\nWe have Received Your Payment.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nHostit Company PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect('welcome')         
        else:
            print(newplan.errors)
    return render(request, 'buy_plan_1099.html',{'user':user,'cuser':cuser})

def buy_1599(request):
    user=request.session.get('user')
    uid=request.session.get('uid')  
    cuser=signupmaster.objects.get(id=uid)
    if request.method == "POST":
        newplan = plan_form(request.POST, request.FILES)
        if newplan.is_valid():
            newplan.save()
            print("Plan saved")
            # send mail
            sub="Thank you"
            message = f"Hello {request.POST['fullname']}! \n\nWe have Received Your Payment.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nHostit Company PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect('welcome')         

        
        else:
            print(newplan.errors)
    return render(request, 'buy_plan_1599.html',{'user':user,'cuser':cuser})

def buy_2099(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=signupmaster.objects.get(id=uid)
    if request.method == "POST":
        newplan = plan_form(request.POST, request.FILES)
        if newplan.is_valid():
            newplan.save()
            print("Plan saved")
            # send mail
            sub="Thank you"
            message = f"Hello {request.POST['fullname']}! \n\nWe have Received Your Payment.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nHostit Company PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
            return redirect('welcome')         

        
        else:
            print(newplan.errors)
    return render(request, 'buy_plan_2099.html',{'user':user,'cuser':cuser})


def membar_page(request):
    return render(request,"membar_page.html") 

def userlogout(request):
    logout(request)
    return redirect('/')

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=signupmaster.objects.get(id=uid)
    if request.method=='POST':
        newuser=updateForm(request.POST,instance=cuser)
        if newuser.is_valid():
            newuser.save()
            print("Profile updated!")
            return redirect("welcome")
        else:
            print(newuser.errors)
    return render(request,'update_profile.html',{'user':user,'cuser':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        newfeedback = Feedback_form(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Feedback saved")
            # send mail
            sub="Thank you"
            message = f"Hello {request.POST['name']}! \n\nWe have Received Your feedback.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nHostit Company PVT. LTD.\n Mo: +91 99791 31476"
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['dhrutidharkotadiya99@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
        
        
        
        else:
            print(newfeedback.errors)
    return render(request,'contact.html')

def price(request):
    return render(request,'price.html')

def service(request):
    return render(request,'service.html')


@shared_task
def send_plan_expiration_reminder():
    # Get users whose plan is expiring in 5 days
    expiration_date = timezone.now() + timedelta(days=5)
    users_to_remind = plan.objects.filter(expiration_date=plan.date)

    for user_plan in users_to_remind:
        user = user_plan.user
        # email_subject = 'Your plan is expiring soon'
        # email_context = {'user': user, 'expiration_date': expiration_date}
        # email_body = render_to_string(email_context)
        # send_mail(email_subject, email_body, 'dhrutidharkotadiya51@gmail.com',)

        sub="Thank you"
        message = f"Your plan is expiring soon \n\nIf any Queries, plz feel free to contact us...\nRegards \nHostit Company PVT. LTD.\n Mo: +91 99791 31476"
        frm_mail = settings.EMAIL_HOST_USER
        to_mail=['dhrutidharkotadiya99@gmail.com',  [user.email]]
        send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)



