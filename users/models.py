from django.contrib.auth.models import AbstractUser
from django.db import models

from speciality.models import Speciality

NULLABLE = {'blank': True, 'null': True}


PATIENT = 'patient'
DOCTOR = 'doctor'

ROLES = (
    (PATIENT, 'Пациент'),
    (DOCTOR, 'Врач')
)


class User(AbstractUser):
    """
    Класс для Пользователя.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users_avatar/', verbose_name='аватар пользователя', **NULLABLE)
    first_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия пользователя')
    date_of_birth = models.DateField(verbose_name='дата рождения', **NULLABLE)
    email_verify = models.BooleanField(default=False)
    role = models.CharField(verbose_name='Роль', choices=ROLES, default=PATIENT, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Строковое представление модели пользователя.
        """
        return f'{self.first_name} {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Doctor(models.Model):
    """
    Класс для врача.
    """

    user = models.OneToOneField(User, verbose_name='Врач', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, verbose_name='Специализация', **NULLABLE)
    education = models.TextField(verbose_name='Образование')
    experience = models.IntegerField(verbose_name='Стаж работы', **NULLABLE)

    def __str__(self):
        """
        Строковое представление модели Врач.
        """
        return f'{self.user.first_name} {self.user.last_name}. Специализация: {self.user.doctor.speciality}'

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
