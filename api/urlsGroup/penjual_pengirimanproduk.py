from django import urls
from django.urls import path
from api.viewsGroup.penjual_pengiriman.create import create
from api.viewsGroup.penjual_pengiriman.delete import delete
from api.viewsGroup.penjual_pengiriman.listById import listById
from api.viewsGroup.penjual_pengiriman.update import update
from api.viewsGroup.penjual_pengiriman.imageUpload import imageUpload
from api.viewsGroup.penjual_pengiriman.listActive import listActive
from api.viewsGroup.penjual_pengiriman.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]