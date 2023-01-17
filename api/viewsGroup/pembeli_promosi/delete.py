from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from api.database.pembeli.promosi import PembeliPromosi
from django.conf import settings
import os


@csrf_exempt
def delete(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        dataRequest = json.loads(request.body.decode("utf-8"))

        # GET DATA BANNER BASED ON ID
        dataPembeliPromosi = PembeliPromosi.objects.get(id=dataRequest["id"])

        # HAPUS YANG LAMA
        old_image_link = dataPembeliPromosi.image_link

        # REMOVE OLD FILE
        try:
            os.remove(settings.MEDIA_ROOT_DELETE + str(old_image_link))
        except:
            pass

        PembeliPromosi.objects.filter(id=dataRequest["id"]).delete()

        return HttpResponse("success")
    else:
        return HttpResponse("failed")
