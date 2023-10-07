from django.shortcuts import render

# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import PortfolioSerializer, ProjectSerializer
from .models import Portfolio, Project


# Create a viewset
class PortfolioViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Portfolio.objects.all()

    # specify serializer to be used
    serializer_class = PortfolioSerializer


# Create a viewset
class ProjectViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Project.objects.all()

    # specify serializer to be used
    serializer_class = ProjectSerializer
