# coding=utf-8
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context_processors import csrf
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, SearchForm1, CommentForm, UserProfile
from django.core.paginator import Paginator


def post_list(request, page_number=1):
    if request.method == "GET":
        form = SearchForm1(request.GET)
        if form.is_valid():
            if form.cleaned_data['name'] and form.cleaned_data['surname'] and form.cleaned_data['fam']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), name__contains=form.cleaned_data['name'], surname__contains=form.cleaned_data['surname'], fam__contains=form.cleaned_data['fam']).order_by('-published_date')
                current_page = Paginator(posts, 4)
            elif form.cleaned_data['name'] and form.cleaned_data['surname']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), name__contains=form.cleaned_data['name'], surname__contains=form.cleaned_data['surname']).order_by('-published_date')
                current_page = Paginator(posts, 4)
            elif form.cleaned_data['name'] and form.cleaned_data['fam']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), name__contains=form.cleaned_data['name'], fam__contains=form.cleaned_data['fam']).order_by('-published_date')
                current_page = Paginator(posts, 4)
            elif form.cleaned_data['surname'] and form.cleaned_data['fam']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), surname__contains=form.cleaned_data['surname'], fam__contains=form.cleaned_data['fam']).order_by('-published_date')
                current_page = Paginator(posts, 4)
            elif form.cleaned_data['name']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), name__contains=form.cleaned_data['name']).order_by('-published_date')
                current_page = Paginator(posts, 4)
            elif form.cleaned_data['surname']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), surname__contains=form.cleaned_data['surname']).order_by('-published_date')
                current_page = Paginator(posts, 4)
            elif form.cleaned_data['fam']:
                posts = Post.objects.filter(published_date__lte=timezone.now(), fam__contains=form.cleaned_data['fam']).order_by('-published_date')
                current_page = Paginator(posts, 4)

            else:
                posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
                current_page = Paginator(posts, 4)
            return render(request, 'blog/post_list.html', {'posts': current_page.page(page_number), 'form': form})
    else:
        form = SearchForm1()

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    current_page = Paginator(posts, 4)
    return render(request, 'blog/post_list.html', {'posts': current_page.page(page_number), 'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.name and not post.surname and not post.fam:
                post.name = 'Имя неизвестно'
            post.save()
            return redirect('app.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.name and not post.surname and not post.fam:
                post.name = 'Имя неизвестно'
            post.published_date = timezone.now()
            post.save()
            return redirect('app.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request, page_number=1):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    current_page = Paginator(posts, 4)
    return render(request, 'blog/post_draft_list.html', {'posts': current_page.page(page_number)})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('app.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('app.views.post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = auth.get_user(request).username
            comment.save()
            return redirect('app.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('registration/register.html', args)


def user_profile(request):
    user = auth.get_user(request)
    # first_name = user.first_name
    # last_name = user.last_name
    args = {}
    args.update(csrf(request))
    if request.POST:
        user_form = UserProfile(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        form = UserProfile(instance=user)
        form.first_name = 'DAsdasd'
        args['form'] = form
    return render_to_response('blog/user_profile.html', args)

