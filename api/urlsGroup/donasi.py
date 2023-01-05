from django import urls
from django.urls import path
from api.viewsGroup.donasi.create import create
from api.viewsGroup.donasi.list import list
from api.viewsGroup.donasi.listById import listById
from api.viewsGroup.donasi.update import update
from api.viewsGroup.donasi.imageUpload import imageUpload
from api.viewsGroup.donasi.listActive import listActive
from api.viewsGroup.donasi.delete import delete

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]