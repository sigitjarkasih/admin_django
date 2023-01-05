from django import urls
from django.urls import path
from api.viewsGroup.article.create import create
from api.viewsGroup.article.list import list
from api.viewsGroup.article.listById import listById
from api.viewsGroup.article.update import update
from api.viewsGroup.article.delete import delete
from api.viewsGroup.article.listActive import listActive
from api.viewsGroup.article.imageUpload import imageUpload

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("list-active/", listActive),
    path("image-upload/", imageUpload),
]