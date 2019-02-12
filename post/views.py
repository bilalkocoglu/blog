from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()
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
        post = form.save()
        messages.success(request, "Post basarili bir sekilde olusturuldu !")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'post/create.html', context)

def post_delete(request, id):

    if not request.user.is_authenticated():
        messages.error(request, "Bu islem icin yetkiniz yok !")
        return post_index(request)

    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Post basarili bir sekilde silindi.')
    return redirect('post:index')

def post_update(request, id):
    if not request.user.is_authenticated():
        messages.error(request, "Bu islem icin yetkiniz yok !")
        return post_index(request)
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, "Post basarili bir sekilde guncellendi !")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, 'post/create.html', context)

def post_detail(request, postId):
    post = get_object_or_404(Post, id = postId)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html', context)
