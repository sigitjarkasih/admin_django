from django import urls
from django.urls import path
from api.viewsGroup.article_staycation.create import create
from api.viewsGroup.article_staycation.list import list
from api.viewsGroup.article_staycation.listById import listById
from api.viewsGroup.article_staycation.update import update
from api.viewsGroup.article_staycation.imageUpload import imageUpload
from api.viewsGroup.article_staycation.listActive import listActive
from api.viewsGroup.article_staycation.delete import delete

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]