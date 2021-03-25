from pathlib import Path
from django.shortcuts import render

from .models import BlogPost, Review

app_name = Path("blog")
# Create your views here.
def index(request):
    blogposts = BlogPost.objects.all().order_by("-publication_date")
    return render(request, app_name / "index.html", {
        "blogposts": blogposts
    })

def article(request, article_id):
    article = BlogPost.objects.get(pk=article_id)
    reviews = article.review_set.all()
    return render(request, app_name / "article.html", {
        "article": article,
        "reviews": reviews
    })
