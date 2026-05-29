from django.shortcuts import render, redirect
from .models import Blog, Favblog
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def displaypage(request):
    displayblog = Blog.objects.all()
    return render(request, 'app/display.html', {'displayblog': displayblog})


def readmore(request, id):
    readblog = Blog.objects.get(id=id)
    return render(request, 'app/readblog.html', {'readblog': readblog})


class CreateBlog(CreateView):
    model = Blog
    fields = ['title', 'desc', 'price', 'img']
    template_name = 'app/createblog.html'


class editblog(UpdateView):
    model = Blog
    fields = ['title', 'desc', 'price', 'img']
    template_name = 'app/editblog.html'


class Deleteblog(DeleteView):
    model = Blog
    template_name = 'app/deleteblog.html'
    success_url = reverse_lazy('displaypage')


class deletefav(DeleteView):
    model = Favblog
    template_name = 'app/deletefav.html'
    success_url = reverse_lazy('displaypage')


def favblog(request):

    if request.method == 'POST':
        favblogid = request.POST.get('fav')

        blogget = Blog.objects.get(id=favblogid)

        Favblog.objects.get_or_create(
            user=request.user,
            blog=blogget
        )

    favblogs = Favblog.objects.filter(user=request.user)

    return render(request, 'app/fav.html', {'favblog': favblogs})
