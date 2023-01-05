from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import DgmallArticle
import json
import uuid


@csrf_exempt
def create(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        id = uuid.uuid1()
        DgmallArticle.objects.create(
            id=id.hex
        )
        obj = DgmallArticle.objects.get(id=id.hex)

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
