from msilib.schema import ListView

from django.http import HttpResponse
from django.shortcuts import render
from students.models import MyModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'students/contact.html')
