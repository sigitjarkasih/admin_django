import json
import uuid
from api.models import DgmallUserArticle
from django.db import connection
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        countEmailUsed = DgmallUserArticle.objects.filter(
            email=data["email"]).count()
        if countEmailUsed == 0:
            cursor = connection.cursor()
            id = uuid.uuid1()
            query = """
                    INSERT INTO dgmall_user_client
                        (id, email, password, token_id, created_at, updated_at)
                    VALUES
                        (%s, %s, %s, 0, '',
                        NOW(), NOW())
                    """
            cursor.execute(
                query,
                [id.hex, data["email"], data["password"]]
            )

            return HttpResponse("success")
        else:
            return HttpResponse("Email has been registered")
    else:
        return HttpResponse("failed")
