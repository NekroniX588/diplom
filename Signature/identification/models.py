from django.db import models
from django.core.files.storage import FileSystemStorage

class Signature(models.Model):
	author = models.CharField(max_length=200, verbose_name='Название')
	attach = models.FileField(storage=FileSystemStorage(location='sign'))
# Create your models here.
