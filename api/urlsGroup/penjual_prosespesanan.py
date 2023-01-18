from django import urls
from django.urls import path
from api.viewsGroup.penjual_prosespesanan.create import create
from api.viewsGroup.penjual_prosespesanan.delete import delete
from api.viewsGroup.penjual_prosespesanan.listById import listById
from api.viewsGroup.penjual_prosespesanan.update import update
from api.viewsGroup.penjual_prosespesanan.imageUpload import imageUpload
from api.viewsGroup.penjual_prosespesanan.listActive import listActive
from api.viewsGroup.penjual_prosespesanan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]