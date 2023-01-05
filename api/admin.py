from django.contrib import admin
from api.database.dgmall.dgmall_donasi import DgmallDonasi
# Register your models here.
from api.database.dgmall.article_login import ArticleLogin

class DgmallDonasiAdmin(admin.ModelAdmin):
    pass

class DgmallLoginAdmin(admin.ModelAdmin):
    pass


admin.site.register(DgmallDonasi)
admin.site.register(ArticleLogin)