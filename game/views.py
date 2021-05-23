from django.shortcuts import render, redirect
from .forms import TopBackForm
from .forms import ZayavkaForm
from django.views.generic import View


def contact(request):
    return render(request, 'contact.html')

class TopBackView(View):
    def post(self, request):
        form = TopBackForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")




class ZayavkaView(View):
    def post(self, request):
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
