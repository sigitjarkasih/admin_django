from django import urls
from django.urls import path
from api.viewsGroup.penjual_fiturpenjualan.create import create
from api.viewsGroup.penjual_fiturpenjualan.delete import delete
from api.viewsGroup.penjual_fiturpenjualan.listById import listById
from api.viewsGroup.penjual_fiturpenjualan.update import update
from api.viewsGroup.penjual_fiturpenjualan.imageUpload import imageUpload
from api.viewsGroup.penjual_fiturpenjualan.listActive import listActive
from api.viewsGroup.penjual_fiturpenjualan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]