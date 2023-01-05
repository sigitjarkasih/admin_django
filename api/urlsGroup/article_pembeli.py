from django import urls
from django.urls import path
from api.viewsGroup.article_pembeli.create import create
from api.viewsGroup.article_pembeli.delete import delete
from api.viewsGroup.article_pembeli.listById import listById
from api.viewsGroup.article_pembeli.update import update
from api.viewsGroup.article_pembeli.imageUpload import imageUpload
from api.viewsGroup.article_pembeli.listActive import listActive
from api.viewsGroup.article_pembeli.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]