from django.shortcuts import render

from datetime import datetime

from appeals_novoross.views import direction_identifier
from .models import Apeals, Subject, ApealsComments
from .forms import ApealsCommentsForm

from django_mailbox.models import Message

# Create your views here.
def index(request):

      return True

def apeals(request):
      messages = Message.objects.filter(read=None)

      for message in messages:

            recognized_data = direction_identifier(message.text)

            author, created = Subject.objects.get_or_create(
                  email = message.from_address[0]
            )
            print(author.id)
            message.read = datetime.now()
            message.save()
            Apeals.objects.create(subject=author, content=message.text, destination=recognized_data[1][1], topic=recognized_data[0][1])

      data = {
            'apeals': Apeals.objects.all().order_by('-id')
      }

      return render(request, "apeals_list.html", context={"data": data})

def apeals_details(request, apeals_id):

      if "add_notice" in request.POST:

                contact_notice_form = NoticeForm(request.POST)

                if contact_notice_form.is_valid():

                    add_notice(contact_notice_form, Apeals.objects.get(id=apeals_id), 0)
      
      comment_form = ApealsCommentsForm()

      data = {
            'apeals_data': Apeals.objects.get(id=apeals_id),
            'comment_form': comment_form
      }
      return render(request, "apeals_details.html", context={"data": data})


def add_notice(form, model_object, type, status, message=False):
    notice = form.save(commit=False)
    notice.type = type
    notice.status = status
    if message != False:
        notice.message = message
    notice.save()