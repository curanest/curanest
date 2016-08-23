from rest_framework import serializers
from .models import ContactUs, AgentQuery 

class ContactusSerializers(serializers.ModelSerializer):
	class Meta:
		model = ContactUs
		fields = ('id','subject','message','email','mobilenumber')

class AgentQuerySerializers(serializers.ModelSerializer):
	#agent = serializers.RelatedField(many=True, read_only=True)
	class Meta:
		model = AgentQuery
		fields = '__all__'
