from django.contrib import admin
from .models import PatientProfile, AgentProfile, HospitalProfile, PatientInfo, Query, AgentQuery, NewAgentQuery, HospitalQuery, HospitalImages, QueryImages, ContactUs
from ratings.handlers import ratings, RatingHandler
from ratings.forms import StarVoteForm
from ratings.forms import SliderVoteForm

class QueriesInLine(admin.TabularInline):
    model = Query
    extra = 0

class AgentQueriesInLine(admin.TabularInline):
    model = NewAgentQuery
    extra = 0


class PatientProfileAdmin(admin.ModelAdmin):
    #list_display = ['user','date_of_birth','gender','created','updated','_queries']
    list_display = ['user','date_of_birth','gender','_queries']
    
    inlines = [
        QueriesInLine
    ]

    def _queries(self, obj):
        return obj.queries.all().count()

class AgentProfileAdmin(admin.ModelAdmin):
    #list_display = ['user','date_of_birth','gender','created','updated','_queries']
    list_display = ['user','date_of_birth','gender','_queries']
    
    inlines = [
        AgentQueriesInLine
    ]

    def _queries(self, obj):
        return obj.queries.all().count()

class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','gender']

class HospitalQueriesInLine(admin.TabularInline):
    model = HospitalQuery
    extra = 1

class HospitalImagesInLine(admin.TabularInline):
    model = HospitalImages
    extra = 1

class HospitalProfileAdmin(admin.ModelAdmin):
    list_display = ['user','address']

    inlines = [
        HospitalQueriesInLine, HospitalImagesInLine,
    ]

class QueryImagesInLine(admin.TabularInline):
    model = QueryImages
    extra = 1

class QueryAdmin(admin.ModelAdmin):
    list_display = ['message']

    inlines = [
        HospitalQueriesInLine, QueryImagesInLine,
    ]

class NewAgentQueryAdmin(admin.ModelAdmin):
    list_display = ['message']

admin.site.register(PatientProfile, PatientProfileAdmin) 
admin.site.register(AgentProfile) 
#admin.site.register(DoctorProfile, DoctorProfileAdmin) 
admin.site.register(HospitalProfile, HospitalProfileAdmin) 
admin.site.register(AgentQuery)
#admin.site.register(NewAgentQuery,NewAgentQueryAdmin)
admin.site.register(HospitalImages)
admin.site.register(QueryImages)
admin.site.register(ContactUs)
admin.site.register(PatientInfo)
ratings.register(HospitalProfile,score_range=(1, 10), form_class=SliderVoteForm)
