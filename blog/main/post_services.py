from .models import Post


def post_all():
    all_posts = Post.objects.all()
    return all_posts
