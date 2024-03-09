from django.db import models

# Create your models here.

class signupmaster(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=30)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    gmail=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class plan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=50)
    connection = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    mob = models.BigIntegerField()
    email = models.EmailField()
    my_files = models.FileField(upload_to='Payment_Screenshot')
    plan = models.CharField(max_length=10)
    date = models.DateField()
    status = models.CharField(max_length=20)


class feedback(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phn = models.BigIntegerField()
    msg = models.TextField()


class complain(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mob = models.BigIntegerField()
    complain_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    # my_files = models.FileField(upload_to='Complaint_Screenshot')
    

class subscribe(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    email = models.EmailField()
    

    