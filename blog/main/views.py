from django.http import JsonResponse
from django.shortcuts import redirect, render
from faker import Faker

from .authors_services import authors
from .form import PostForm, SubscribeForm
from .models import Author
from .post_services import post_all
from .subsribers_services import sub_all


def index(request):
    return render(request, "main/index.html", {"title": "Home Page"})


def about(request):
    return render(request, "main/about.html", {"title": "About company"})


def posts(request):
    return render(request, "main/posts.html", {"title": "Posts", "posts": post_all()})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "main/post_create.html", context=context)


def authors_all(request):
    return render(request, "main/authors.html", {"title": "Authors", "authors": authors()})


def authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return redirect("authors_all")


def authors_sub(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subscribers_all")
    else:
        form = SubscribeForm()
    context = {
        "form": form,
    }
    return render(request, "main/authors_subscribe.html", context=context)


def subscribers_all(request):
    return render(request, "main/subscribers.html", {"title": "Subscribers", "subscribers": sub_all()})


def api_response(request):
    all_posts = post_all()
    posts_list = list(all_posts.values())
    return JsonResponse(posts_list, safe=False)
