from django import urls
from django.urls import path
from api.viewsGroup.article_login.create import create
from api.viewsGroup.article_login.delete import delete
from api.viewsGroup.article_login.listById import listById
from api.viewsGroup.article_login.update import update
from api.viewsGroup.article_login.imageUpload import imageUpload
from api.viewsGroup.article_login.listActive import listActive
from api.viewsGroup.article_login.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]