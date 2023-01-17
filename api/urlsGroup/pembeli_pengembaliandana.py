from django import urls
from django.urls import path
from api.viewsGroup.pembeli_pengembaliandana.create import create
from api.viewsGroup.pembeli_pengembaliandana.delete import delete
from api.viewsGroup.pembeli_pengembaliandana.listById import listById
from api.viewsGroup.pembeli_pengembaliandana.update import update
from api.viewsGroup.pembeli_pengembaliandana.imageUpload import imageUpload
from api.viewsGroup.pembeli_pengembaliandana.listActive import listActive
from api.viewsGroup.pembeli_pengembaliandana.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]