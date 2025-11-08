from rest_framework import serializers
from .models import Task
from .models import User
from .models import Grup

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'start_time',
            'end_time',
            'status',
            'created_at'
        ]

class GrupSerializer(serializers.ModelSerializer):
    task_title = serializers.CharField(source='task.title', read_only=True)
    
    members = serializers.SerializerMethodField()

    
    class Meta:
        model = Grup
        fields = ['id', 'sef','task_title','members']

    def get_members(self, obj):
        users = User.objects.filter(usergrup__grup=obj)
        
        return [str(user) for user in users]

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # Am adăugat 'username' în lista de câmpuri
        fields = ['username', 'email', 'nume', 'prenume', 'password', 'telefon', 'manager']

    def create(self, validated_data):
        user = User.objects.create_user(
            # Am adăugat 'username' și aici
            username=validated_data['username'],
            email=validated_data['email'],
            nume=validated_data['nume'],
            prenume=validated_data['prenume'],
            password=validated_data['password'],
            telefon=validated_data.get('telefon'),
            manager=validated_data.get('manager')
        )
        return user