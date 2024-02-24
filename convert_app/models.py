from django.db import models

# Create your models here.
class uploaded_file(models.Model):
    file=models.FileField(upload_to="uploads/")