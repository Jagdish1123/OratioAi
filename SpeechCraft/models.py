# models.py

from django.db import models

class SaveAudio(models.Model):
    record = models.FileField(upload_to='audio_recordings')
