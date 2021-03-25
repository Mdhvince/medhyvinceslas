from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def unauthenticated_only(view_func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('blog:index'))
        return view_func(request, *args, **kwargs)
    
    return inner