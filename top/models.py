from django.db import models
from datetime import datetime


class FileModel(models.Model):
    src_file = models.FileField(upload_to='src')
    dst_file = models.FileField(upload_to='dst')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,editable=True)
    user_id = models.UUIDField()
