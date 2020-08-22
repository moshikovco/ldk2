from django.contrib.postgres.fields import ArrayField
from django.utils.crypto import get_random_string
from django.db import models
from model_utils import Choices
from phone_field import PhoneField
from datetime import datetime
from api.models import ExternalForm

class Subject(models.Model):
      first_name = models.CharField(null=True, blank=True, max_length=64, verbose_name="Имя")
      midle_name = models.CharField(null=True, blank=True, max_length=64, verbose_name="Отчество")
      last_name = models.CharField(null=True, blank=True, max_length=64, verbose_name="Фамилия")
      gender = models.CharField(null=True, blank=True, max_length=64, verbose_name="Пол")
      phone = PhoneField(null=True, blank=True, verbose_name="Телефон", unique=True)
      email = models.EmailField(null=True, blank=True, max_length=128, verbose_name="Email")
      addres = models.CharField(null=True, blank=True, max_length=256, verbose_name="Адрес")
      addres_arr = models.TextField(null=True, blank=True)

      delo_id = models.IntegerField(verbose_name="Дело ID пользователя", default=0)

      def __str__(self):
            return f"{self.first_name} {self.last_name}"



class Apeals(models.Model):
      STATUSES = Choices(
            (0, 'new', 'Новое'),
            (1, 'woked', 'В работе'),
            (2, 'redirect', 'Перенаправлено'),
            (3, 'response', 'Требуется ответ гражданина'),
            (10, 'closed', 'Завершено'),
      )
      FORMAT = Choices(
            (0, 'forms', 'Обращения с формы'),
            (1, 'email', 'Email обращения'),
            (2, 'phone', 'Входящий звонок')
      )
      subject = models.ForeignKey(
            Subject,
            on_delete=models.CASCADE,
            related_name="subject",
            related_query_name="subject",
            null=True, blank=True

      )
      form = models.ForeignKey(
            ExternalForm,
            on_delete=models.CASCADE,
            related_name="form",
            related_query_name="form",
            null=True, blank=True
      )
      content = models.TextField(verbose_name="Текст обращения", default="Без сообщения")
      file = models.FileField(verbose_name="Файл", null=True, blank=True)
      destination = models.CharField(max_length=128, verbose_name="Адресат обращения", null=True, blank=True)
      topic = models.CharField(max_length=128, verbose_name="Тема обращения", null=True, blank=True)
      status = models.IntegerField(choices=STATUSES, default=0)
      format = models.IntegerField(choices=FORMAT, default=0)
      created = models.DateTimeField(default=datetime.now())
      updated = models.DateTimeField(auto_now=True)
      reminder = models.DateTimeField(null=True, blank=True)

      uid = models.CharField(max_length=16, default=get_random_string(length=8))

      delo_id = models.IntegerField(verbose_name="Дело ID обращения", default=0)


class ApealsComments(models.Model):
      TYPES = Choices(
            (0, 'system', 'Системное сообщение'),
            (1, 'message', 'Сообщение'),
      )
      apeals = models.ForeignKey(
            Apeals,
            on_delete=models.CASCADE,
            related_name="apeal",
            related_query_name="apeal"
      )
      message = models.TextField(null=True)
      type = models.IntegerField(choices=TYPES, default=1)
      created = models.DateTimeField(default=datetime.now())