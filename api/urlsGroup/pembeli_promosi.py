from django import urls
from django.urls import path
from api.viewsGroup.pembeli_promosi.create import create
from api.viewsGroup.pembeli_promosi.delete import delete
from api.viewsGroup.pembeli_promosi.listById import listById
from api.viewsGroup.pembeli_promosi.update import update
from api.viewsGroup.pembeli_promosi.imageUpload import imageUpload
from api.viewsGroup.pembeli_promosi.listActive import listActive
from api.viewsGroup.pembeli_promosi.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]