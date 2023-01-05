from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from api.database.dgmall.article_event import ArticleEvent
from django.conf import settings
import os


@csrf_exempt
def delete(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        dataRequest = json.loads(request.body.decode("utf-8"))

        # GET DATA BANNER BASED ON ID
        dataArticle = ArticleEvent.objects.get(id=dataRequest["id"])

        # HAPUS YANG LAMA
        old_image_link = dataArticle.image_link

        # REMOVE OLD FILE
        try:
            os.remove(settings.MEDIA_ROOT_DELETE + str(old_image_link))
        except:
            pass

        ArticleEvent.objects.filter(id=dataRequest["id"]).delete()

        return HttpResponse("success")
    else:
        return HttpResponse("failed")
