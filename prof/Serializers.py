from rest_framework import serializers
from .models import ContactUs, AgentQuery, AgentProfile 

class ContactusSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id','subject','message','email','mobilenumber')

class AgentQuerySerializers(serializers.ModelSerializer):
    class Meta:
        model = AgentQuery
        fields = '__all__'

    # def create(self, validated_data):
    #     print 'hello'

class AgentProfileSerializers(serializers.ModelSerializer):
    queries = AgentQuerySerializers(many=True, read_only=True)
    class Meta:
        model = AgentProfile
        fields = '__all__'

    def create(self, validated_data):
        queries_data = validated_data.pop('queries')
        agent = AgentProfile.objects.create(**validated_data)
        for query_data in queries_data:
            AgentQuery.objects.create(user=agent, **query_data)
        return agent



    

