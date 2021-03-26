from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_blog"),
    path("<int:article_id>", views.article, name="article")
]