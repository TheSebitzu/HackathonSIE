# In api/views.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
from .models import User
from .serializers import UserRegisterSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Grup, UserGrup, UserTask
from .serializers import GrupSerializer 
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Grup, UserGrup, UserTask, Task
from django.contrib.auth import get_user_model
from .models import Grup
from .serializers import GrupSerializer

User = get_user_model()

# -----------------------------------------------
# 1. THE FUNCTION TO CREATE A GROUP
# -----------------------------------------------
@api_view(['POST'])
def create_group(request):
    from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Grup, UserGrup, UserTask, Task
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def create_group(request):
    
    data = request.data
    name = data.get("name")
    member_ids = data.get("member_ids", [])
    task_id = data.get("task_id")

    if not name or not member_ids or not task_id:
        return Response({"error": "Toate campurile sunt obligatorii"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        task_obj = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    # Creează grup
    grup = Grup.objects.create(name=name, task=task_obj)

    # Dacă sunt membri selectați, îi adaugăm
    if member_ids:
        for uid in member_ids:
            try:
                user = User.objects.get(id=uid)
                UserGrup.objects.create(user=user, grup=grup)
                
                # Dacă există task, îl atribuim membrilor
                if task_id:
                    try:
                        task = Task.objects.get(id=task_id)
                        UserTask.objects.create(user=user, task=task)
                    except Task.DoesNotExist:
                        pass
            except User.DoesNotExist:
                pass

    return Response({
        "success": True,
        "group_id": grup.id,
        "name": f"Grup {grup.id}",
        "members": member_ids,
        "task_id": task_id
    }, status=status.HTTP_201_CREATED)



User = get_user_model() 

class UserTaskListView(APIView):
    def get(self, request):
        users = [{"id": u.id, "name": str(u)} for u in User.objects.all()]
        tasks = TaskSerializer(Task.objects.all(), many=True).data
        return Response({"users": users, "tasks": tasks})



class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer

class GroupListView(generics.ListAPIView):
    """
    API view to list all groups (Grup).
    """
    queryset = Grup.objects.all()
    serializer_class = GrupSerializer
    permission_classes = [permissions.AllowAny]