from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from api.database.pembeli.komplainpesanan import PembeliKomplain


@csrf_exempt
def update(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        obj = PembeliKomplain.objects.get(id=data["id"])

        try:
            obj.master_judul = data["master_judul"]
        except:
            pass

        try:
            obj.title = data["title"]
        except:
            pass

        try:
            obj.content_desc = data["content_desc"]
        except:
            pass

        try:
            obj.is_active = data["is_active"]
        except:
            pass

        obj.save()

        return HttpResponse("success")
    else:
        return HttpResponse("failed")
