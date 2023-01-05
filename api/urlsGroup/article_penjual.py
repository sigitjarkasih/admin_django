from django import urls
from django.urls import path
from api.viewsGroup.article_penjual.create import create
from api.viewsGroup.article_penjual.delete import delete
from api.viewsGroup.article_penjual.listById import listById
from api.viewsGroup.article_penjual.update import update
from api.viewsGroup.article_penjual.imageUpload import imageUpload
from api.viewsGroup.article_penjual.listActivate import listActive
from api.viewsGroup.article_penjual.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]