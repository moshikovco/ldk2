from django import forms
from django.forms import CharField, ModelForm

import json 

from .models import ExternalForm
from dashboard.models import Apeals, Subject

class ExternalApealsForm(forms.ModelForm):

      # form = forms.IntegerField()
      author = forms.CharField(label='Ваше имя')
      phone = forms.CharField(label='Телефон')
      email = forms.EmailField(label='Электронная почта')
      addres = forms.CharField(label='Ваш адрес')
      dadata_fio = forms.CharField(widget=forms.HiddenInput(), required=False)
      dadata_addres = forms.CharField(widget=forms.HiddenInput(), required=False)
      user_id = forms.CharField(widget=forms.HiddenInput(), required=False)

      class Meta:
            model = Apeals
            fields = ('content', 'file', 'form')

            widgets = {
                  'content': forms.Textarea(attrs={'data-toggle': 'autosize', 'rows': '3'}),
                  'subject': forms.NumberInput()
            }
            labels = {
                'content': 'Обращение',
                'file': 'Добавить файл (PDF, Фото/Видео)',

            }


      
      def __init__(self, uid, *args, **kwargs):
            super(ExternalApealsForm, self).__init__(*args, **kwargs)
            # print(uid)
            # self.fields['form'].initial = ExternalForm.objects.get(uid=uid)
            # print(self.fields['form'])

      def save(self, commit=True):
            author_info = json.loads(self.cleaned_data['dadata_fio'])
            author_addres = json.loads(self.cleaned_data['dadata_addres'])
            
            author, created = Subject.objects.get_or_create(
                  first_name = author_info['data']['name'],
                  phone = self.cleaned_data['phone'],
                  
            )
            
            if created:
                  author.midle_name = json.dumps(author_info['data']['patronymic']),
                  author.last_name = json.dumps(author_info['data']['surname']),
                  author.gender = json.dumps(author_info['data']['gender']),
                  author.email = self.cleaned_data['email'],
                  author.addres = json.dumps(author_addres['value'])
                  author.save()

            self.cleaned_data['subject'] = author.id
            


            return super(ExternalApealsForm, self).save(commit)
