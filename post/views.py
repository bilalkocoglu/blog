# -*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.db.models import Q

def post_index(request):
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter( Q(title__icontains=query) |
                                      Q(content__icontains=query) |
                                      Q(user__first_name__icontains=query) |
                                      Q(user__last_name__icontains=query)
                                      ).distinct()

    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts
    }
    return render(request, 'post/index.html', context)

def post_create(request):

    if not request.user.is_authenticated():
        messages.error(request, "Bu islem icin yetkiniz yok !")
        return post_index(request)

    #if request.method=="POST":
    #    print (request.POST)

    #title = request.POST.get('title')      Bu yontem uygulanabilir fakat tavsiye edilmez
    #content = request.POST.get('content')
    #Post.objects.create(title=title, content=content)

    #if request.method == 'POST':
    #    #post olusturma islemi yapilmali
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #else:
    #    #sadece create sayfasina yonlendirme yapilacak
    #    form = PostForm()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, "Post basarili bir sekilde olusturuldu !")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'post/create.html', context)

def post_delete(request, slug):

    if not request.user.is_authenticated():
        messages.error(request, "Bu islem icin yetkiniz yok !")
        return post_index(request)

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post basarili bir sekilde silindi.')
    return redirect('post:index')

def post_update(request, slug):
    if not request.user.is_authenticated():
        messages.error(request, "Bu islem icin yetkiniz yok !")
        return post_index(request)
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, "Post basarili bir sekilde guncellendi !")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, 'post/create.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, "Yorum basarili bir sekilde eklendi !")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'post/detail.html', context)
