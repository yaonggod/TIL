from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality':60})
    