from django.db import models
from datetime import datetime

class DgmallArticle(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=500)
    content_desc = models.TextField(null=True, blank=True)
    is_active = models.SmallIntegerField(default=0)
    image_link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "dgmall_article"

    def __str__(self):
        return "{}".format(self.id)

class DgmallUserArticle(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    email = models.CharField(null=True, blank=True,max_length=50, default=None)
    password = models.CharField(null=True, blank=True, max_length=20, default=None)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "dgmall_user_article"

    def __str__(self):
        return "{}".format(self.id)