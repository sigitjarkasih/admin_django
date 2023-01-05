from django import urls
from django.urls import path
from api.viewsGroup.dgmall_donasi.create import create
from api.viewsGroup.dgmall_donasi.list import list
from api.viewsGroup.dgmall_donasi.listById import listById
from api.viewsGroup.dgmall_donasi.update import update
from api.viewsGroup.dgmall_donasi.imageUpload import imageUpload
from api.viewsGroup.dgmall_donasi.listActive import listActive
from api.viewsGroup.dgmall_donasi.delete import delete

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]