from django import urls
from django.urls import path
from api.viewsGroup.akun_keamanan.create import create
from api.viewsGroup.akun_keamanan.delete import delete
from api.viewsGroup.akun_keamanan.listById import listById
from api.viewsGroup.akun_keamanan.update import update
from api.viewsGroup.akun_keamanan.imageUpload import imageUpload
from api.viewsGroup.akun_keamanan.listActive import listActive
from api.viewsGroup.akun_keamanan.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]