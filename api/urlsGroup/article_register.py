from django import urls
from django.urls import path
from api.viewsGroup.article_register.create import create
from api.viewsGroup.article_register.delete import delete
from api.viewsGroup.article_register.listById import listById
from api.viewsGroup.article_register.update import update
from api.viewsGroup.article_register.imageUpload import imageUpload
from api.viewsGroup.article_register.listActive import listActive
from api.viewsGroup.article_register.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]