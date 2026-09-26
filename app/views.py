from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

# Create your views here.

#Create Student ---> CreateView
class StdCreateView(CreateView):
    model = Student
    template_name = "form.html"
    fields = [
        "name",
        "roll",
        "dept",
        "address",
        "phone"
    ]

    success_url = reverse_lazy("list")


#Student List ---> ListView
class StdListView(ListView):
    model = Student
    template_name = "list.html"
    context_object_name = "stds"


#Student Detail ---> DetailView
class StdDetailView(DetailView):
    model = Student
    template_name = "details.html"
    context_object_name = "std"


#Edit Student --> UpdataView
class StdUpdateView(UpdateView):
    model = Student
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("list")


#Delete Student ---> DeleteView
class StdDeleteView(DeleteView):
    model = Student
    template_name = "delete.html"
    success_url = reverse_lazy('list')