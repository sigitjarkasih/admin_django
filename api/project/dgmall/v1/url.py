from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.project.dgmall.v1.machine.userClient.screen import screen as userClientScreen

urlpatterns = [
    path("user-client/", userClientScreen),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)