from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from prof.models import ContactUs,AgentProfile,AgentQuery
#<<<<<<< HEAD
from .serializers import ContactUsSerializer, AgentQueryCreateSerializer#, AgentProfileCreateSerializer,
# =======
# from .serializers import ContactUsSerializer, AgentQueryCreateSerializer, AgentProfileCreateSerializer
# from django.contrib.auth.models import User
# import random
# >>>>>>> ef57d6dfc36652db4fb58388a8d5887316b505f7

class ContactUsListAPIView(ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsRetrieveAPIView(RetrieveAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsUpdateAPIView(UpdateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsDeleteAPIView(DestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsCreateAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    # def perform_create(self,serializer):
    #   agent = AgentProfile.objects.get(user=self.request.user)
    #   print agent
    #   serializer.save(agent=agent)

class AgentQueryCreateAPIView(CreateAPIView):
# <<<<<<< HEAD
    queryset = AgentQuery.objects.all()
    serializer_class = AgentQueryCreateSerializer

    def perform_create(self,serializer):
        agent = AgentProfile.objects.get(user=self.request.user)
        print agent
        serializer.save(agent=agent)

# class AgentProfileCreateAPIView(CreateAPIView):
#     queryset = AgentProfile.objects.all()
#     serializer_class = AgentProfileCreateSerializer

#     def perform_create(self,serializer):
#         #user = User.objects.create_user('name','email@gmail.com','password')
#         #serializer.save(user=user)
#         serializer.save()
# =======
# 	queryset = AgentQuery.objects.all()
# 	serializer_class = AgentQueryCreateSerializer

# 	def perform_create(self,serializer):
# 		agent = AgentProfile.objects.get(user=self.request.user)
# 		print agent
# 		serializer.save(agent=agent)

# class AgentProfileCreateAPIView(CreateAPIView):
# 	queryset = AgentProfile.objects.all()
# 	serializer_class = AgentProfileCreateSerializer

# 	def perform_create(self,serializer):
# 		serializer.is_valid()
# 		print serializer.validated_data
# 		user = User.objects.create_user('name121'+str(random.randint(1,100)),'email112'+ str(random.randint(1,100)) +'@gmail.com','password')
# 		serializer.save(user=user)
# >>>>>>> ef57d6dfc36652db4fb58388a8d5887316b505f7
