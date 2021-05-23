from django import forms
from .models import TopBack

from .models import Zayavka

class TopBackForm(forms.ModelForm):
      class Meta:
          model = TopBack
          fields = ['name', 'description', 'email', 'phone']


class ZayavkaForm(forms.ModelForm):
      class Meta:
          model = Zayavka
          fields = ['name', 'description', 'email', 'phone']
