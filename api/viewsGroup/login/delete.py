from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import DgmallUserArticle
import json


@csrf_exempt
def delete(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        DgmallUserArticle.objects.filter(id=data["id"]).delete()

        return HttpResponse("success")
    else:
        return HttpResponse("failed")