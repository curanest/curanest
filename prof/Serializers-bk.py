from rest_framework import serializers
from .models import ContactUs, AgentQuery, AgentProfile 

class ContactusSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id','subject','message','email','mobilenumber')

class AgentProfileSerializer(ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'

class AgentQuerySerializers(serializers.ModelSerializer):
    class Meta:
        model = AgentQuery
        fields = '__all__'




    

