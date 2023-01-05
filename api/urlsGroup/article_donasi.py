from django import urls
from django.urls import path
from api.viewsGroup.article_donasi.create import create
from api.viewsGroup.article_donasi.list import list
from api.viewsGroup.article_donasi.listById import listById
from api.viewsGroup.article_donasi.update import update
from api.viewsGroup.article_donasi.imageUpload import imageUpload
from api.viewsGroup.article_donasi.listActivate import listActive
from api.viewsGroup.article_donasi.delete import delete

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]