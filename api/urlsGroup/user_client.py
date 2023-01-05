from django import urls
from django.urls import path
from api.viewsGroup.login.create import create
from api.viewsGroup.login.loginByEmail import loginByEmail
from api.viewsGroup.login.delete import delete
from api.viewsGroup.login.listById import  listById
from api.viewsGroup.login.list import list

urlpatterns = [
    path("listbyid/", listById),
    path("create/", create),
    path("delete/", delete),
    path("login-by-email/", loginByEmail),
    path("list/", list),

]