from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.database.penjual.lainnyapenjual import LainnyaPenjual
import json
import uuid


@csrf_exempt
def create(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        id = uuid.uuid1()
        LainnyaPenjual.objects.create(
            id=id.hex
        )
        obj = LainnyaPenjual.objects.get(id=id.hex)

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

        try:
            obj.image_link = data["image_link"]
        except:
            pass

        obj.save()

        return HttpResponse(id.hex)
    else:
        return HttpResponse("failed")
