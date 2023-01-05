from django import urls
from django.urls import path
from api.viewsGroup.article_akadtransaksi.create import create
from api.viewsGroup.article_akadtransaksi.delete import delete
from api.viewsGroup.article_akadtransaksi.listById import listById
from api.viewsGroup.article_akadtransaksi.update import update
from api.viewsGroup.article_akadtransaksi.imageUpload import imageUpload
from api.viewsGroup.article_akadtransaksi.listActive import listActive
from api.viewsGroup.article_akadtransaksi.list import list

urlpatterns = [
    path("list/", list),
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("update/", update),
    path("image-upload/", imageUpload),
    path("list-activate/", listActive),
]