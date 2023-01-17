from django import urls
from django.urls import path
from api.viewsGroup.pembeli_komplainpesanan.create import create
from api.viewsGroup.pembeli_komplainpesanan.delete import delete
from api.viewsGroup.pembeli_komplainpesanan.listById import listById
from api.viewsGroup.pembeli_komplainpesanan.update import update
from api.viewsGroup.pembeli_komplainpesanan.imageUpload import imageUpload
from api.viewsGroup.pembeli_komplainpesanan.listActive import listActive
from api.viewsGroup.pembeli_komplainpesanan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]