from .models import Signature

from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UploadForm(forms.ModelForm):
 
	class Meta:
		model = Signature
		fields = ['author', 'attach']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'