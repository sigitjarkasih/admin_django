from django.db import models
from datetime import datetime

class Article_donasi(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    master_judul= models.CharField(null=True, blank=True,max_length=100, default=None)
    title = models.TextField(null=True, blank=True)
    content_desc = models.TextField(null=True, blank=True)
    is_active = models.SmallIntegerField(default=0)
    image_link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "article_donasi"

    def __str__(self):
        return "{}".format(self.id)