from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import DgmallUserArticle
import json
import uuid


@csrf_exempt
def loginByEmail(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        obj = DgmallUserArticle.objects.filter(
            email=data["email"],
            password=data["password"]
        ).count()

        if obj > 0:
            objClient = DgmallUserArticle.objects.get(email=data["email"])
            token_id = objClient.token_id

            if(token_id == '' or token_id == None):
                token_id = uuid.uuid1()
                objClient.token_id = token_id.hex
                objClient.save()

                result = token_id.hex
            else:
                result = token_id
        else:
            result = 'failed'

        return HttpResponse(result)

    else:
        return HttpResponse("failed")

