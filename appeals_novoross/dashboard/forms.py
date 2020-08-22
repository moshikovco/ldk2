from django import forms
from django.forms import CharField, ModelForm

from .models import ApealsComments

class ApealsCommentsForm(forms.ModelForm):

      class Meta:
            model = ApealsComments
            fields = ('message', )

            widgets = {
                  'message': forms.Textarea(attrs={'placeholder': 'Комментарий', 'data-toggle': 'autosize', 'rows': '3', 'maxlength': '250', 'oninput': '$("#message_counter").text($(this).val().length+"/250")'}),
            }