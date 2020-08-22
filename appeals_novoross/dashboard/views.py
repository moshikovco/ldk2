from django.shortcuts import render

from datetime import datetime

import requests

from appeals_novoross.views import direction_identifier
from .models import Apeals, Subject, ApealsComments
from .forms import ApealsCommentsForm, ApealsDetailsForm, ApealsFilter

from django_mailbox.models import Message


# * Методы
# Для автоматического сбора писем с электронных ящиков необходимо настроить CRON задачу на выполение python manage.py getmail

def index(request):

      return render(request, "dashboard.html", context={"data": 'data'})

def apeals(request):
      #* Получение и обработка входящих емейлов
      messages = Message.objects.filter(read=None)

      for message in messages:

            message_title = str(message)
            print(message_title)
            recognized_data = direction_identifier(message.text)

            author, created = Subject.objects.get_or_create(
                  email = message.from_address[0]
            )
            
            message.read = datetime.now()
            message.save()

            # Сохранение емейла как обращения
            Apeals.objects.create(subject=author, content=message_title+" - "+message.text, destination=recognized_data[1][1], topic=recognized_data[0][1], format = 1)

      apeals_filter = ApealsFilter(request.GET, queryset=Apeals.objects.all())
      # Данные для вывода
      data = {
            'apeals': apeals_filter
      }


      return render(request, "apeals_list.html", context={"data": data})

def apeals_details(request, apeals_id):

      cApeal = Apeals.objects.get(id=apeals_id)
      if "add_comment" in request.POST:

                comment_form = ApealsCommentsForm(request.POST)

                if comment_form.is_valid():

                    add_comment(comment_form, cApeal, 1)

      if "update_apeals" in request.POST:
            
            apeals_detail = ApealsDetailsForm(request.POST, instance=cApeal) 

            if apeals_detail.is_valid():
                  apeals_detail.save()
                  add_comment(ApealsCommentsForm(), cApeal, 0, 'Обращение обновлено')

      apeals_detail_form = ApealsDetailsForm(instance=cApeal)
      comment_form = ApealsCommentsForm()

      data = {
            'apeals_data': cApeal,
            'apeals_form': apeals_detail_form,
            'comments': ApealsComments.objects.filter(apeals=apeals_id),
            'comment_form': comment_form
      }
      return render(request, "apeals_details.html", context={"data": data})


def add_comment(form, model_object, type, message=False):
    comment = form.save(commit=False)
    comment.apeals = model_object
    comment.type = type
    if message != False:
        comment.message = message
    comment.save()

    send_sms(type)

# Отправка тестовых СМС через SMS.RU
def send_sms(type, phone = 79180325232):
      if type == 0:
            url = f"https://sms.ru/sms/send?api_id=A49CFEEC-E148-B593-53B7-44FB89DD73B1&to={phone},&msg=Обращение+обновлено+ld.moshikov.co/apeals/E24H0V3Cu&json=1"
      else: 
            url = f"https://sms.ru/sms/send?api_id=A49CFEEC-E148-B593-53B7-44FB89DD73B1&to={phone},&msg=Вы+получили+новое+сообщение+к+своему+обращению+ld.moshikov.co/apeals/E24H0V3Cu&json=1"

      payload  = {}
      headers= {}

      response = requests.request("POST", url, headers=headers, data = payload)