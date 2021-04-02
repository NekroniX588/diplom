from django.shortcuts import render

from .models import Signature
from .forms import UploadForm

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class NewSignatureCreate(CreateView): # новый
	model = Signature
	form_class = UploadForm
	template_name = 'signature_add.html'
	success_url = reverse_lazy('main')
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super().form_valid(form)

def main(request):
	context = {}
	template = 'main.html'
	return render(request, template, context)
# Create your views here.
