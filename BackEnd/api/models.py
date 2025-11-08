from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# =========================================
# User personalizat
# =========================================
class UserManager(BaseUserManager):
    def create_user(self, email, nume, prenume, password=None, telefon=None, manager=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, nume=nume, prenume=prenume, telefon=telefon, manager=manager)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nume, prenume, password=None):
        user = self.create_user(email, nume, prenume, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nume', 'prenume']

    def __str__(self):
        return f"{self.nume} {self.prenume}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

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
    sef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='seful_grupului')

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
