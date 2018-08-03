from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv/school_detail.html'

class SchoolCreateView(CreateView):
	fields = ('name', 'principal', 'location')
	model = models.School

class SchoolUpdateView(UpdateView):
	# limit what fields you can update
	fields = ('name', 'principal')
	model = models.School

class SchoolDeleteView(DeleteView):
	model = models.School
	# After successful delete, go back to list page and show all schools minus recently deleted
	success_url = reverse_lazy("cbv:list")

