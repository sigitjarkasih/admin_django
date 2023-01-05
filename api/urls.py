from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .urlsGroup import article, user_client

urlpatterns = [
    # url untuk API endpoint
    path("v1/article/", include(article.urlpatterns)),
    path("v1/user_article/", include(user_client.urlpatterns)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)