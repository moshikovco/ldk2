from django import forms
from django.forms import CharField, ModelForm
import django_filters

from .models import Apeals, ApealsComments

class ApealsDetailsForm(forms.ModelForm):

      class Meta:
            model = Apeals
            fields = ('status', 'topic', 'destination')

            labels = {
                'status': 'Статус',
            }

class ApealsCommentsForm(forms.ModelForm):

      class Meta:
            model = ApealsComments
            fields = ('message', )

            widgets = {
                  'message': forms.Textarea(attrs={'placeholder': 'Комментарий', 'data-toggle': 'autosize', 'rows': '3', 'maxlength': '250', 'oninput': '$("#message_counter").text($(this).val().length+"/250")'}),
            }
            labels = {
                'message': 'Сообщение пользователю',
            }

# Фильтр обращений
class ApealsFilter(django_filters.FilterSet):
    class Meta:
        model = Apeals
        fields = ['status', 'format', 'created']