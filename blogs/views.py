from django.shortcuts import render

# Create your views here.
def blogs(request):
    return render(request, 'blogs/blogs.html')


def blog(request):
    return render(request, 'blogs/blog.html')


def search(request):
    return render(request, 'blogs/search.html')