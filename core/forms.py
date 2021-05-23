from django import forms
from django.forms import Textarea
from .models import Articles,Comments
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('category','name', 'text', 'price','image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AuthUserForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Логин'
            self.fields['password'].label = 'Пароль'

            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = ('username', 'password')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text','user_photo','user_name','user_firstname')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['text'].widget = Textarea(attrs={'rows':5})
