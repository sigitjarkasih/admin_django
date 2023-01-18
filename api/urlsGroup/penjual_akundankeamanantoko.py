from django import urls
from django.urls import path
from api.viewsGroup.penjual_akundankeamanan.create import create
from api.viewsGroup.penjual_akundankeamanan.delete import delete
from api.viewsGroup.penjual_akundankeamanan.listById import listById
from api.viewsGroup.penjual_akundankeamanan.update import update
from api.viewsGroup.penjual_akundankeamanan.imageUpload import imageUpload
from api.viewsGroup.penjual_akundankeamanan.listActive import listActive
from api.viewsGroup.penjual_akundankeamanan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]