from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import time
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from api.database.penjual.pengirimanproduk import PengirimanProduk


@csrf_exempt
def imageUpload(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        # GET POST REQUEST
        id = request.POST["id"]
        upload_file = request.FILES["image"]

        # GET DATA BANNER BASED ON ID
        dataPenjualPengirimanProduk = PengirimanProduk.objects.get(id=id)
                
        # HAPUS YANG LAMA
        old_image_link = dataPenjualPengirimanProduk.image_link

        # REMOVE OLD FILE
        try:
            os.remove(settings.MEDIA_ROOT_DELETE + str(old_image_link))
        except:
            pass

        # GET EXTENSION
        extension = os.path.splitext(upload_file.name)[1]

        # SET NEW FILENAME
        new_filename = str(int(round(time.time() * 1000))) + extension

        # UPLOAD NEW PHOTO TO MEDIA
        fs = FileSystemStorage()
        fs.save("pengiriman_produk/" + new_filename, upload_file)

        # UPDATE RECORD
        dataPenjualPengirimanProduk.image_link = "/media/pengiriman_produk/" + new_filename
        dataPenjualPengirimanProduk.save()

        return HttpResponse('success')
