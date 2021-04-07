from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home_page"),
    path("posts", views.posts, name="posts"),
    path("posts/create", views.post_create, name="post_create"),

    path("authors/new", views.authors_new, name="authors_new"),
    path("authors/all", views.authors_all, name="authors_all"),
    path("authors/subscribe", views.authors_sub, name="authors_sub"),

    path("subscribers/all", views.subscribers_all, name="subscribers_all"),

    path("api/posts", views.api_response, name="api_response"),

    path("about", views.about, name="about"),
]
