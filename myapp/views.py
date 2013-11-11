from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from myapp.models import Blog
from django.http import Http404

def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response("myapp/blog_list.html", {"blogs": blogs})

def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("myapp/blog_show.html", {"blog": blog})