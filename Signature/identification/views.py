import os
import numpy as np
from .inference import get_embedding

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
		embed = get_embedding(self.object.attach.path)
		if os.path.exists('./checkpoints/embeddings.npy'):
			embeddings = np.load('./checkpoints/embeddings.npy')
			embeddings = np.append(embeddings, embed, axis=0)
		else:
			embeddings = embed
		print('embeddings shape:', embeddings.shape)
		np.save('./checkpoints/embeddings', embeddings)
		return super().form_valid(form)

def main(request):
	context = {}
	template = 'main.html'
	return render(request, template, context)
# Create your views here.
