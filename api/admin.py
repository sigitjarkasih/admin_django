from django.contrib import admin
from .models import DgmallArticle, DgmallUserArticle
# Register your models here.

class DgmallArticleAdmin(admin.ModelAdmin):
    pass

class DgmallUserArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(DgmallArticle, DgmallArticleAdmin)
admin.site.register(DgmallUserArticle, DgmallUserArticleAdmin)