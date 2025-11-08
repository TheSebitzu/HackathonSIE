from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet,
    RegisterUserView,
    GroupListView,
    create_group,
    UserTaskListView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # <-- Importăm view-ul standard
    TokenRefreshView
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/grupuri/', GroupListView.as_view(), name='grupuri-list'),
    path('api/groups/create/', create_group, name='create-group'),
    path('api/users-tasks/', UserTaskListView.as_view(), name='users-tasks-list'),
]
