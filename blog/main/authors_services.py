from .models import Author


def authors():
    all_authors = Author.objects.all()
    return all_authors
