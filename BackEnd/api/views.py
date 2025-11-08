from django.shortcuts import render
from rest_framework.permissions import AllowAny


# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
