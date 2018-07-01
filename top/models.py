from django.db import models
from datetime import datetime
import os

def src_upload_to(instance, filename):
    return os.path.join('src', str(instance.user_id), filename)

class FileModel(models.Model):
    user_id = models.UUIDField()
    src_file = models.FileField(upload_to=src_upload_to)
    dst_file = models.FileField(upload_to='dst')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,editable=True)

