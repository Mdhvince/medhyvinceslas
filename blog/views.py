from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost, Review
from .forms import ReviewForm

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

    form = ReviewForm()
    if request.method == "POST":
        post = request.POST.copy() # to make it mutable
        post.update({'author': request.user, 'blog_post': article_id})
        request.POST = post

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:article', args=(article_id,)))

    context = {"form": form, "article": article, "reviews": reviews}
    return render(request, app_name / "article.html", context)
