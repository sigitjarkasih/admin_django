from django import urls
from django.urls import path
from api.viewsGroup.article_dompetmadrasah.create import create
from api.viewsGroup.article_dompetmadrasah.delete import delete
from api.viewsGroup.article_dompetmadrasah.listById import listById
from api.viewsGroup.article_dompetmadrasah.update import update
from api.viewsGroup.article_dompetmadrasah.imageUpload import imageUpload
from api.viewsGroup.article_dompetmadrasah.listActivate import listActive
from api.viewsGroup.article_dompetmadrasah.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]