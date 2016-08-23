from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.conf import settings
from django.contrib.auth.models import User

def get_usertype(self):
    return self.usertype

def set_usertype(self,usertype):
    self.usertype = usertype

User.add_to_class("set_usertype",set_usertype)
User.add_to_class("get_usertype",get_usertype)

class PatientProfile(models.Model):
    usertype = models.CharField(max_length=20,null=True)
    GENDER = (
        ('male','Male'),
        ('female','Female'),
        )

    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=10,choices=GENDER,default='male')
    allergies = models.CharField(max_length=50,null=True)
    medicalhistory = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=False,null=True)
    mobilenumber = models.CharField(max_length=15,null=True)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    

    def __unicode__(self):
        return self.user.username

class AgentProfile(models.Model):
    GENDER = (
        ('male','Male'),
        ('female','Female'),
        )

    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=10,choices=GENDER,default='male')
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=False,null=True)
    mobilenumber = models.CharField(max_length=15,null=True)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __unicode__(self):
        return self.user.username

class HospitalProfile(models.Model):
    #pid = models.AutoField(max_length=10,primary_key=True,default=None)
    user = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=False,null=True)
    mobilenumber = models.CharField(max_length=15,default=None)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    ratings = GenericRelation(Rating, related_query_name='ratings')

    def __unicode__(self):
        return self.user.username


class Query(models.Model):
    user = models.ForeignKey(PatientProfile,related_name='queries')
    agent = models.ForeignKey(AgentProfile,related_name='agent_queries')
    message = models.TextField()
    hospital = models.ManyToManyField(HospitalProfile,through='HospitalQuery')
    
    def __unicode__(self):
        return self.message

class PatientInfo(models.Model):
    query = models.OneToOneField(Query)
    email = models.EmailField(max_length=30)
    mobilenumber = models.CharField(max_length=15)

class AgentQuery(models.Model):
    agent = models.ForeignKey(AgentProfile,related_name='queries')
    message = models.TextField()
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    mobilenumber = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.mobilenumber

class NewAgentQuery(models.Model):
    pass
    # user = models.ForeignKey(AgentProfile,related_name='agent_queries')
    # message = models.TextField()
    # email = models.EmailField(max_length=30)
    # mobilenumber = models.CharField(max_length=15)
    
    # def __unicode__(self):
    #     return self.mobilenumber

class HospitalQuery(models.Model):
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)

    def __unicode__(self):
        return "Hello"

class HospitalImages(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    hospital = models.ForeignKey(HospitalProfile,related_name='hospital_images')

class QueryImages(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    query = models.ForeignKey(Query,related_name='query_images')

# class AgentQueryImages(models.Model):
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     query = models.ForeignKey(AgentQuery,related_name='agent_query_images')

class ContactUs(models.Model):
    subject = models.CharField(max_length=30)
    message = models.TextField()
    email = models.EmailField(max_length=30)
    mobilenumber = models.CharField(max_length=15) 

    def __unicode__(self):
        return self.subject + ' ' + self.mobilenumber  