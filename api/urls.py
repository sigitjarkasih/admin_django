from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .urlsGroup import (
   article_akadtransaksi, article_dompetmadrasah, article_donasi, article_event, article_login, article_pembeli, article_penjual, article_register, article_staycation, article_syariaharea,
   akun_keamanan, pembeli_pesanan, pembeli_pembayaran, pembeli_pengiriman, pembeli_pengembaliandana, pembeli_komplainpesanan, pembeli_promosi, pembeli_lainnya,
   penjual_akundankeamanantoko, penjual_fiturpenjualan, penjual_komplainpesanantoko, penjual_lainnya, penjual_pengirimanproduk, penjual_prosespesanan
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
#PEMBELI
     path("v1/akun-keamanan/", include(akun_keamanan.urlpatterns)),
     path("v1/pembeli-pesanan/", include(pembeli_pesanan.urlpatterns)),
     path("v1/pembeli-pembayaran/", include(pembeli_pembayaran.urlpatterns)),
     path("v1/pembeli-pengiriman/", include(pembeli_pengiriman.urlpatterns)),
     path("v1/pembeli-pengembaliandana/", include(pembeli_pengembaliandana.urlpatterns)),
     path("v1/pembeli-komplainpesanan/", include(pembeli_komplainpesanan.urlpatterns)),
     path("v1/pembeli-promosi/", include(pembeli_promosi.urlpatterns)),
     path("v1/pembeli-lainnya/", include(pembeli_lainnya.urlpatterns)),
#PENJUAL
     path("v1/akunkeamanan-toko/", include(penjual_akundankeamanantoko.urlpatterns)),
     path("v1/fiturpenjualan-toko/", include(penjual_fiturpenjualan.urlpatterns)),
     path("v1/komplainpesanan-toko/", include(penjual_komplainpesanantoko.urlpatterns)),
     path("v1/penjual-lainnya/", include(penjual_lainnya.urlpatterns)),
     path("v1/pengiriman-produk/", include(penjual_pengirimanproduk.urlpatterns)),
     path("v1/proses-pesanan/", include(penjual_prosespesanan.urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)