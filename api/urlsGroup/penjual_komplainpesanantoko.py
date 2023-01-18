from django import urls
from django.urls import path
from api.viewsGroup.penjual_komplainpesanan.create import create
from api.viewsGroup.penjual_komplainpesanan.delete import delete
from api.viewsGroup.penjual_komplainpesanan.listById import listById
from api.viewsGroup.penjual_komplainpesanan.update import update
from api.viewsGroup.penjual_komplainpesanan.imageUpload import imageUpload
from api.viewsGroup.penjual_komplainpesanan.listActive import listActive
from api.viewsGroup.penjual_komplainpesanan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]