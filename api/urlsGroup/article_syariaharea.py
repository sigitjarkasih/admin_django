from django import urls
from django.urls import path
from api.viewsGroup.article_syariaharea.create import create
from api.viewsGroup.article_syariaharea.list import list
from api.viewsGroup.article_syariaharea.listById import listById
from api.viewsGroup.article_syariaharea.update import update
from api.viewsGroup.article_syariaharea.imageUpload import imageUpload
from api.viewsGroup.article_syariaharea.listActive import listActive
from api.viewsGroup.article_syariaharea.delete import delete

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]