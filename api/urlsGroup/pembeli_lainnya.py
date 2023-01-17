from django import urls
from django.urls import path
from api.viewsGroup.pembeli_lainnya.create import create
from api.viewsGroup.pembeli_lainnya.delete import delete
from api.viewsGroup.pembeli_lainnya.listById import listById
from api.viewsGroup.pembeli_lainnya.update import update
from api.viewsGroup.pembeli_lainnya.imageUpload import imageUpload
from api.viewsGroup.pembeli_lainnya.listActive import listActive
from api.viewsGroup.pembeli_lainnya.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]