from django.urls import reverse
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
# ['GET'=list]
# ['POST'=Create]
# ['PUT'=Update]
# ['PATCH']
from .models import Car
from .serializers import CarSerializer

class CarListApiView(ListAPIView):
    gueryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateApiView(CreateAPIView):
    gueryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_clases = [IsAuthenticated | IsAdminUser]

class CarUpdateApiView(UpdateAPIView):
    gueryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteApiView(DestroyAPIView):
    gueryset = Car.objects.all()
    serializer_class = CarSerializer


