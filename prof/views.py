from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.forms import inlineformset_factory
from .models import Query, AgentQuery, PatientProfile, PatientInfo, AgentProfile, HospitalProfile, HospitalQuery, QueryImages #, Image
from .forms import QueryForm, QueryImageForm, AgentQueryForm, EmailPhoneForm, ProfileEditForm, PatientProfileEditForm,  UserRegistrationForm, MailForm, ContactUsForm
 #,ImageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory


class HospitalProfileView(DetailView):
    model = HospitalProfile

    def get_object(self, queryset=None):
        obj = HospitalProfile.objects.get(user__username=self.kwargs.get("hospital"))
        return get_object_or_404(HospitalProfile, pk=obj.id)
        #obj, created = self.model.objects.get_or_create(bar='foo bar baz')
        #return obj

    # def get_context_data(self, **kwargs):
    #     print kwargs['object']
    #     kwargs['sizes'] = {object: self.model.objects.get_or_create(user__username=kwargs['object'])}
    #     return super(HospitalProfileView, self).get_context_data(**kwargs)

# class SizesView(TemplateView):
#     model = HospitalProfile
#     template_name = 'sizes.html'

#     def get_context_data(self, **kwargs):
#         print 'SizesView'
#         kwargs['sizes'] = {size: self.model.objects.get_or_create(bar=str(size))[0] for size in range(10, 40)}
#         return super(SizesView, self).get_context_data(**kwargs)

def query(request,hospital=None):
    
    agent = False

    if not request.user.is_anonymous():
        if AgentProfile.objects.filter(user=request.user).exists():
            agent = True
        elif PatientProfile.objects.filter(user=request.user).exists():
            agent = False
        else:
            print 'Error'

    QueryImageFormSet = modelformset_factory(QueryImages,
                                        form=QueryImageForm, extra=3)
    if hospital is not None:
        hospital_obj = HospitalProfile.objects.get(user__username=hospital)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #pp = PatientProfile(user=request.user)
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST)
        formset = QueryImageFormSet(request.POST, request.FILES,
                               queryset=QueryImages.objects.none())

        if request.user.is_anonymous():
            form2 = EmailPhoneForm(request.POST)
            if form2.is_valid():
                user = User.objects.create_user(form2.cleaned_data['email'], form2.cleaned_data['email'], form2.cleaned_data['email'])
                pp = PatientProfile(user=user)
                pp.save()
                pp = PatientProfile.objects.get(user=user)

        # elif agent:
        #     form2 = AgentQueryForm(request.POST)
        #     if form2.is_valid():
        #         pass

                #patientInfo = PatientInfo.objects.create(email=form2.cleaned_data['email'], mobilenumber=form2.cleaned_data['mobilenumber'],query= )
                #patientInfo.save()

        else:
            if agent:
                form2 = AgentQueryForm(request.POST)
                pp = AgentProfile.objects.get(user=request.user)
            else:
                pp = PatientProfile.objects.get(user=request.user)

        # check whether it's valid:
        if form.is_valid() and formset.is_valid():

            p = form.save(commit=False)
            if not agent:
                p.agent_id = pp.user_id
                p.user = pp
            else:
                p.user_id = pp.user_id
                p.agent = pp

            p.save()


            if agent and form2.is_valid():
                patientInfo = PatientInfo.objects.create(email=form2.cleaned_data['email'], mobilenumber=form2.cleaned_data['mobilenumber'],query=p )
                patientInfo.save() 
                
            
            if hospital is not None:
                HospitalQuery.objects.create(hospital=hospital_obj,query=p)

            for form in formset.cleaned_data:
                if not form:
                    continue
                print 'dssds',form
                image = form['photo']
                photo = QueryImages(query=p, photo=image)
                photo.save()

            return render(request, 'done.html', locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        if request.user.is_anonymous():
            form2 = EmailPhoneForm()
        if agent:
            form2 = AgentQueryForm()
        form = QueryForm()
        formset = QueryImageFormSet(queryset=QueryImages.objects.none())

        return render(request, 'query.html', locals())


# def query(request,hospital=None):
#     #print hospital
#     #print request.user.get_usertype()
#     # if AgentProfile.objects.filter(user=request.user).exists():
#     #     agent = True
#     # elif PatientProfile.objects.filter(user=request.user).exists():
#     #     agent = False
#     # else:
#     #     print 'Error'

#     QueryImageFormSet = modelformset_factory(QueryImages,
#                                         form=QueryImageForm, extra=3)
#     if hospital is not None:
#         hospital_obj = HospitalProfile.objects.get(user__username=hospital)

#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         #pp = PatientProfile(user=request.user)
#         # create a form instance and populate it with data from the request:
#         if agent:
#             form = AgentQueryForm(request.POST)
#             # formset = QueryImageFormSet(request.POST, request.FILES,
#             #                    queryset=AgentQueryImages.objects.none())
#         else:
#             form = QueryForm(request.POST)
#             formset = QueryImageFormSet(request.POST, request.FILES,
#                                queryset=QueryImages.objects.none())
        
#         if request.user.is_anonymous():
#             form2 = EmailPhoneForm(request.POST)
#             if form2.is_valid():
#                 user = User.objects.create_user(form2.cleaned_data['email'], form2.cleaned_data['email'], form2.cleaned_data['email'])
#                 pp = PatientProfile(user=user)
#                 pp.save()

#         else:
#             pp = PatientProfile(user=request.user)
#             # if agent:
#             #     pp = AgentProfile(user=request.user)
#             # else:
#             #     pp = PatientProfile(user=request.user)
             
#         # check whether it's valid:
#         if form.is_valid() and formset.is_valid():
#             # process the data in form.cleaned_data as required
#             # redirect to a new URL:
#             p = form.save(commit=False)
        
#             print type(pp),type(p)

#             #Establish link between query form and a user
#             #only for patient
#             # if not agent:
#             #     p.user_id = pp.user_id
            
#             #If user is anonymous, connect him to query object
#             if request.user.is_anonymous():
#                 p.user = pp
            
#             if not agent:
#                 p.user_id = pp.user_id

#             p.save()
#             #pp.queries.add(p)
#             print PatientProfile.objects.all()
#             print Query.objects.all()
#             #Query.objects.create(user=pp,query=p)
#             #PatientProfile.objects.create(user=pp,query=p)   
            
            
#             #Test code
#             #return render(request, 'done.html', locals())

#             if hospital is not None:
#                 HospitalQuery.objects.create(hospital=hospital_obj,query=p)

#             for form in formset.cleaned_data:
#                 if not form:
#                     continue
#                 image = form['photo']
#                 photo = QueryImages(query=p, photo=image)
#                 photo.save()

#             return render(request, 'done.html', locals())

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = QueryForm()
#         formset = QueryImageFormSet(queryset=QueryImages.objects.none())

#         if request.user.is_anonymous():
#             form2 = EmailPhoneForm()
#         if AgentProfile.objects.filter(user=request.user).exists():
#             form = AgentQueryForm()
#             formset = QueryImageFormSet(queryset=QueryImages.objects.none())
        

#         return render(request, 'query.html', locals())

def show_hospitals(request):
    print 'HospitalProfile'
    print Query.objects.all()
    pp = PatientProfile.objects.get(user=request.user)
    print pp.queries.all()

    hospitals = HospitalProfile.objects.all()
    return render(request, 'hospitals.html', locals())

def hospital_details(request,username): 
    hospital = HospitalProfile.objects.get(user__username=username)
    return render(request, 'hospital_details.html', locals())

@login_required 
def edit(request):    
    if request.method == 'POST':
        user_form = ProfileEditForm(instance=request.user,data=request.POST)        
        profile_form = PatientProfileEditForm(instance=PatientProfile.objects.get(user=request.user),data=request.POST,files=request.FILES)        
        if user_form.is_valid() and profile_form.is_valid():            
            user_form.save()            
            profile_form.save()  
            return render(request,'done.html',locals())
    else:
        user_form = ProfileEditForm(instance=request.user)        
        profile_form = PatientProfileEditForm(instance=request.user) 

    return render(request,'edit.html', {'user_form': user_form, 'profile_form': profile_form})

def register(request,usertype):
    print usertype 
    if request.method == 'POST':        
        user_form = UserRegistrationForm(request.POST)  
        print user_form
     
        if user_form.is_valid():           
           # Create a new user object but avoid saving it yet            
           new_user = user_form.save(commit=False)            
           # Set the chosen password                             
           new_user.set_password(user_form.cleaned_data['password'])            
           # Save the User object
           new_user.save()

           if usertype == 'broker':
              profile = AgentProfile.objects.create(user=new_user) 
              #profile.set_usertype('agent')
           elif usertype == 'patient':
              profile = PatientProfile.objects.create(user=new_user)
              #profile.set_usertype('patient')
           else:
              print 'Invalid URL'

        return render(request, 'register_done.html', {'new_user': new_user})    
    else:        
        user_form = UserRegistrationForm()    
        return render(request,'register.html',{'user_form': user_form}) 

def dashboard(request):
    #pp = AgentProfile(user=request.user)
    #print pp.queries
    return render(request,'index.html',locals())

@user_passes_test(lambda u: u.is_superuser)
def sendmail_one(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            text_content = form.cleaned_data['text_content']
            html_content = form.cleaned_data['html_content']
            from_email = 'curanest@gmail.com'
            to = form.cleaned_data['to'].split(',')
            print to
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render(request,'done.html',locals())
    else:
        form = MailForm()

    return render(request,'sendmail.html',locals())

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mobilenumber = form.cleaned_data['mobilenumber']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            from_email = 'curanest@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobilenumber + ' ' + email + ' ' + message, from_email, ['curanest@gmail.com'])
            msg.send()
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = ContactUsForm()
    return render(request,'contactus.html',locals())


def ratings_vote(request):
    #handler = ratings.get_handler(HospitalProfile)
    return render(request,'done.html',locals())