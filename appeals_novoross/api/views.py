from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

from django.forms import inlineformset_factory


from .models import ExternalForm
from dashboard.models import Subject, Apeals

from .forms import ExternalApealsForm


@csrf_exempt
@xframe_options_exempt
def formpage(request, uid):
      print("Старница формы")
      Form = get_object_or_404(ExternalForm, uid=uid)

      if request.method == "POST":
            print('Форма отправлена')
            apeals_form = ExternalApealsForm(uid, request.POST)
            if apeals_form.is_valid():
                  print('Форма ВАЛИДНА')
                  print(apeals_form)
                  apeals = apeals_form.save(commit=False)
                  apeals.form = ExternalForm.objects.get(uid=uid)
                  print(apeals.subject)
                  apeals.save()
      else:
            print('Пустая форма')
            apeals_form = ExternalApealsForm(uid)
            
            print(apeals_form['form'])

      # print(apeals_form)

      # BookFormSet = inlineformset_factory(Subject, Apeals, fields=('first_name', 'title',))

      return render(request, "form_frame.html", context={"form": apeals_form})

def form_insert(request, uid):
      Form = get_object_or_404(ExternalForm, uid=uid)
      code = f'<iframe width="100%" height="950px" src="http://127.0.0.1:8000/api/form/{uid}"></iframe>'
      title = Form.title
      return render(request, "form_insert_code.html", context={"code": code, "title": title})
