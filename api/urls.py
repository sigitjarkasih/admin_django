from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .urlsGroup import (
   article_akadtransaksi, article_dompetmadrasah, article_donasi, article_event, article_login, article_pembeli, article_penjual, article_register, article_staycation, article_syariaharea
)

urlpatterns = [
#ADMIN
    path("v1/akad-transaksi/", include(article_akadtransaksi.urlpatterns)),
    path("v1/dompet-madrasah/", include(article_dompetmadrasah.urlpatterns)),
    path("v1/donasi/", include(article_donasi.urlpatterns)),
    path("v1/event/", include(article_event.urlpatterns)),
    path("v1/login/", include(article_login.urlpatterns)),
    path("v1/pembeli/", include(article_pembeli.urlpatterns)),
    path("v1/penjual/", include(article_penjual.urlpatterns)),
    path("v1/register/", include(article_register.urlpatterns)),
    path("v1/staycation/", include(article_staycation.urlpatterns)),
    path("v1/syariaharea/", include(article_syariaharea.urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)