from django.shortcuts import render
from serializers import MainSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class MainViewSet(ModelViewSet):
	queryset = Main.Objects.all()
	serializers_class = MainSerializer

