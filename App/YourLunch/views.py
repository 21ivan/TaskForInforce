from rest_framework import generics
from .serializers import RegistrationSerializer, UserSerializer, RestaurantSerializer, MenuSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import User, Menu, Restaurant
from django.db.models import Q
from django.conf import settings


# Create your views here.


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Message': 'User created successfully',
                'User': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({'Errors': serializers.as_serializer_error}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantApiView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CurrentDayListApiView(generics.GenericAPIView):
    serializer_class = MenuSerializer

    def get(self, request):
        current_date = settings.CURRENT_DATE.date()
        queryset = Menu.objects.filter(Q(created_at__day=current_date))
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
