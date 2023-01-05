from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import astpy
import json
from django.http import HttpResponse

@csrf_exempt
def list(request):
    # userToken = request.headers.get('Authorization').replace("BASIC ", "")
    if request.method == "POST":
        # dataRequest = json.loads(request.body.decode("utf-8"))
        cursor = connection.cursor()
        query = """
                    SELECT *
                    FROM dgmall_article
                    ORDER BY created_at DESC
                """
        cursor.execute(query)
        data = astpy.dictfetchall(cursor)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("failed")
