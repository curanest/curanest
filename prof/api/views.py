from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from prof.models import ContactUs,AgentProfile,AgentQuery
from .serializers import ContactUsSerializer, AgentQueryCreateSerializer

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
	# 	agent = AgentProfile.objects.get(user=self.request.user)
	# 	print agent
	# 	serializer.save(agent=agent)

class AgentQueryCreateAPIView(CreateAPIView):
	queryset = AgentQuery.objects.all()
	serializer_class = AgentQueryCreateSerializer

	def perform_create(self,serializer):
		agent = AgentProfile.objects.get(user=self.request.user)
		print agent
		serializer.save(agent=agent)