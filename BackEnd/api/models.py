from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    # --- MODIFICAT ---
    def create_user(self, username, email, nume, prenume, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(
            username=username, 
            email=email, 
            nume=nume, 
            prenume=prenume, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # --- MODIFICAT ---
    def create_superuser(self, username, email, nume, prenume, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        username="---"
        user = self.create_user(
            username=username,
            email=email,
            nume=nume,
            prenume=prenume,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # --- ADĂUGAT ---
    username = models.CharField(max_length=100, unique=True)
    
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField(unique=True) # Îl păstrăm ca unic, dar nu e pt login
    telefon = models.CharField(max_length=20, blank=True, null=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    # --- MODIFICAT ---
    USERNAME_FIELD = 'username' # Folosim 'username' pentru login
    REQUIRED_FIELDS = ['email', 'nume', 'prenume'] # 'username' e cerut by default

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

# =========================================
# Task
# =========================================
STATUS_CHOICES = [
    ("in_progress", "In Progress"),
    ("assigned", "Assigned"),
    ("completed", "Completed"),
    ("unassigned", "Unassigned"),
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="unassigned")

    def __str__(self):
        return self.title


# =========================================
# Rand_taskuri (user-task mapping)
# =========================================
class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'task')


# =========================================
# Grup
# =========================================
class Grup(models.Model):
    name = models.CharField(max_length=100, default="Grup Nou")
    sef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='seful_grupului')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, related_name='grupuri')
    
    def __str__(self):
        return f"Grup {self.id}"


# =========================================
# Rand_grupuri (user-group mapping)
# =========================================
class UserGrup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grup = models.ForeignKey(Grup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'grup')
