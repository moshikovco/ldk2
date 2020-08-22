from django import forms
from django.forms import CharField, ModelForm

import json 

from .models import ExternalForm
from dashboard.models import Apeals, Subject

class ExternalApealsForm(forms.ModelForm):

      # form = forms.IntegerField()
      author = forms.CharField()
      phone = forms.CharField()
      email = forms.EmailField()
      addres = forms.CharField()
      dadata_fio = forms.CharField(widget=forms.HiddenInput(), required=False)
      dadata_addres = forms.CharField(widget=forms.HiddenInput(), required=False)
      user_id = forms.CharField(widget=forms.HiddenInput(), required=False)

      class Meta:
            model = Apeals
            fields = ('content', 'file', 'form', 'subject')

            widgets = {
                  'subject': forms.NumberInput()
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
                  author.midle_name = author_info['data']['patronymic'],
                  author.last_name = author_info['data']['surname'],
                  author.gender = author_info['data']['gender'],
                  author.email = self.cleaned_data['email'],
                  author.addres = author_addres['value']
                  author.save()

            self.cleaned_data['subject'] = author.id
            


            return super(ExternalApealsForm, self).save(commit)
