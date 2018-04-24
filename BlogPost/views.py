from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, redirect, render_to_response
from .models import BlogPost
from .form import BlogPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def indexblog(request):
    post = BlogPost.objects.all()
    context = {
        'blogPost': post
    }
    return render(request, 'Indexblog.html', context)


def details(request, id):
    try:
        post = BlogPost.objects.get(id=id)
        context = {
            'post': post
        }
        return render(request, 'Details.html', context)
    except BlogPost.DoesNotExist:
        raise Http404('Post Doesn\'t Exist')


@login_required(login_url='SignIn')
def get_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog_creator = request.user
            post.save()
            messages.success(request, 'Post has been save Sucessfully')
            return HttpResponseRedirect('/BlogPost/MyPost')
        else:
            return render(request, 'BlogPost')
    else:
        form = BlogPostForm()
        return render(request, 'GetPost.html', {'form': form})


@login_required(login_url='SignIn')
def viewpost(request):
    storage = messages.get_messages(request)
    form = BlogPostForm()
    posts = BlogPost.objects.filter(blog_creator_id=request.user.id)
    args = {'form': form, 'posts': posts, 'message': storage}
    return render(request, 'MyPost.html', args)


@login_required(login_url='SignIn')
def editpost(request, pid):
    try:
        if request.method == 'POST':
            instance = BlogPost.objects.get(id=pid)
            form = BlogPostForm(request.POST, instance=instance)
            if form.is_valid():
                post = form.save(commit=False)
                post.save(update_fields={'title', 'content', 'updated_at'})
                messages.success(request, 'Post has been Sucessfully Updated !!')
                return HttpResponseRedirect('/BlogPost/MyPost')
        else:
            instance = BlogPost.objects.get(id=pid)
            form = BlogPostForm(request.POST, instance=instance)
            context = {'message': messages, 'form': form, 'post':instance}
            return render(request, 'EditPost.html', context)
    except BlogPost.DoesNotExist:
        raise Http404('Post Doesn\'t Exist')


@login_required(login_url='SignIn')
def deletepost(request, pid=None):
    try:
        messages.success(request, 'Post has been save Sucessfully')
        postid = BlogPost.objects.get(id=pid)
        delpost = postid.delete()
        storage = messages.get_messages(request)
        form = BlogPostForm()
        posts = BlogPost.objects.filter(blog_creator_id=request.user.id)
        context = {'form': form, 'posts': posts, 'message': storage, 'deletepost': delpost}
        return render(request, 'DeletePost.html', context)
    except BlogPost.DoesNotExist:
        raise Http404('Post Doesn\'t Exist')





