from django import urls
from django.urls import path
from api.viewsGroup.article_event.create import create
from api.viewsGroup.article_event.list import list
from api.viewsGroup.article_event.listById import listById
from api.viewsGroup.article_event.update import update
from api.viewsGroup.article_event.imageUpload import imageUpload
from api.viewsGroup.article_event.listActive import listActive
from api.viewsGroup.article_event.delete import delete

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]