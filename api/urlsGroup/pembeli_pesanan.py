from django import urls
from django.urls import path
from api.viewsGroup.pembeli_pesanan.create import create
from api.viewsGroup.pembeli_pesanan.delete import delete
from api.viewsGroup.pembeli_pesanan.listById import listById
from api.viewsGroup.pembeli_pesanan.update import update
from api.viewsGroup.pembeli_pesanan.imageUpload import imageUpload
from api.viewsGroup.pembeli_pesanan.listActive import listActive
from api.viewsGroup.pembeli_pesanan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]