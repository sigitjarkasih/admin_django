from django import urls
from django.urls import path
from api.viewsGroup.pembeli_pembayaran.create import create
from api.viewsGroup.pembeli_pembayaran.delete import delete
from api.viewsGroup.pembeli_pembayaran.listById import listById
from api.viewsGroup.pembeli_pembayaran.update import update
from api.viewsGroup.pembeli_pembayaran.imageUpload import imageUpload
from api.viewsGroup.pembeli_pembayaran.listActive import listActive
from api.viewsGroup.pembeli_pembayaran.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]