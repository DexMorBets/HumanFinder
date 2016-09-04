# coding=utf-8
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context_processors import csrf
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Post_user, Comment, Comment_user
from .forms import PostForm, PostFormUser, SearchForm1, CommentForm, CommentFormUser, UserProfile
from django.core.paginator import Paginator


def post_list(request, page_number=1):
    if request.method == "GET":
        form = SearchForm1(request.GET)
        if form.is_valid():
            if form.cleaned_data['name'] or form.cleaned_data['surname'] or form.cleaned_data['fam']\
                    or form.cleaned_data['id'] or form.cleaned_data['age'] or form.cleaned_data['height']\
                    or form.cleaned_data['body'] or form.cleaned_data['hair_color'] or form.cleaned_data['eyes_color']\
                    or form.cleaned_data['hat'] or form.cleaned_data['hat_color'] or form.cleaned_data['vverh']\
                    or form.cleaned_data['vverh_color'] or form.cleaned_data['niz'] or form.cleaned_data['niz_color']\
                    or form.cleaned_data['boots'] or form.cleaned_data['boots_color'] or form.cleaned_data['shramy']\
                    or form.cleaned_data['tatu'] or form.cleaned_data['protez'] or form.cleaned_data['konech']:
                kwargs = {'published_date__lte': timezone.now()}
                if form.cleaned_data['id']:
                    kwargs['id'] = form.cleaned_data['id']
                if form.cleaned_data['name']:
                    kwargs['name__contains'] = form.cleaned_data['name']
                if form.cleaned_data['surname']:
                    kwargs['surname__contains'] = form.cleaned_data['surname']
                if form.cleaned_data['fam']:
                    kwargs['fam__contains'] = form.cleaned_data['fam']
                if form.cleaned_data['age']:
                    kwargs['age'] = form.cleaned_data['age']
                if form.cleaned_data['height']:
                    kwargs['height'] = form.cleaned_data['height']
                if form.cleaned_data['body']:
                    kwargs['body'] = form.cleaned_data['body']
                if form.cleaned_data['hair_color']:
                    kwargs['hair_color'] = form.cleaned_data['hair_color']
                if form.cleaned_data['eyes_color']:
                    kwargs['eyes_color'] = form.cleaned_data['eyes_color']
                if form.cleaned_data['hat']:
                    kwargs['hat'] = form.cleaned_data['hat']
                if form.cleaned_data['hat_color']:
                    kwargs['hat_color'] = form.cleaned_data['hat_color']
                if form.cleaned_data['vverh']:
                    kwargs['vverh'] = form.cleaned_data['vverh']
                if form.cleaned_data['vverh_color']:
                    kwargs['vverh_color'] = form.cleaned_data['vverh_color']
                if form.cleaned_data['niz']:
                    kwargs['niz'] = form.cleaned_data['niz']
                if form.cleaned_data['niz_color']:
                    kwargs['niz_color'] = form.cleaned_data['niz_color']
                if form.cleaned_data['boots']:
                    kwargs['boots'] = form.cleaned_data['boots']
                if form.cleaned_data['boots_color']:
                    kwargs['boots_color'] = form.cleaned_data['boots_color']


                if form.cleaned_data['shramy']:
                    kwargs['shramy'] = form.cleaned_data['shramy']
                if form.cleaned_data['tatu']:
                    kwargs['tatu'] = form.cleaned_data['tatu']
                if form.cleaned_data['protez']:
                    kwargs['protez'] = form.cleaned_data['protez']
                if form.cleaned_data['konech']:
                    kwargs['konech'] = form.cleaned_data['konech']
                posts = Post.objects.filter(**kwargs).order_by('-published_date')
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


def post_list_user(request, page_number=1):
    if request.method == "GET":
        form = SearchForm1(request.GET)
        if form.is_valid():
            if form.cleaned_data['name'] or form.cleaned_data['surname'] or form.cleaned_data['fam']\
                    or form.cleaned_data['id'] or form.cleaned_data['age'] or form.cleaned_data['height']\
                    or form.cleaned_data['body'] or form.cleaned_data['hair_color'] or form.cleaned_data['eyes_color']\
                    or form.cleaned_data['hat'] or form.cleaned_data['hat_color'] or form.cleaned_data['vverh']\
                    or form.cleaned_data['vverh_color'] or form.cleaned_data['niz'] or form.cleaned_data['niz_color']\
                    or form.cleaned_data['boots'] or form.cleaned_data['boots_color'] or form.cleaned_data['shramy']\
                    or form.cleaned_data['tatu'] or form.cleaned_data['protez'] or form.cleaned_data['konech']:
                kwargs = {'published_date__lte': timezone.now()}
                if form.cleaned_data['id']:
                    kwargs['id'] = form.cleaned_data['id']
                if form.cleaned_data['name']:
                    kwargs['name__contains'] = form.cleaned_data['name']
                if form.cleaned_data['surname']:
                    kwargs['surname__contains'] = form.cleaned_data['surname']
                if form.cleaned_data['fam']:
                    kwargs['fam__contains'] = form.cleaned_data['fam']
                if form.cleaned_data['age']:
                    kwargs['age'] = form.cleaned_data['age']
                if form.cleaned_data['height']:
                    kwargs['height'] = form.cleaned_data['height']
                if form.cleaned_data['body']:
                    kwargs['body'] = form.cleaned_data['body']
                if form.cleaned_data['hair_color']:
                    kwargs['hair_color'] = form.cleaned_data['hair_color']
                if form.cleaned_data['eyes_color']:
                    kwargs['eyes_color'] = form.cleaned_data['eyes_color']
                if form.cleaned_data['hat']:
                    kwargs['hat'] = form.cleaned_data['hat']
                if form.cleaned_data['hat_color']:
                    kwargs['hat_color'] = form.cleaned_data['hat_color']
                if form.cleaned_data['vverh']:
                    kwargs['vverh'] = form.cleaned_data['vverh']
                if form.cleaned_data['vverh_color']:
                    kwargs['vverh_color'] = form.cleaned_data['vverh_color']
                if form.cleaned_data['niz']:
                    kwargs['niz'] = form.cleaned_data['niz']
                if form.cleaned_data['niz_color']:
                    kwargs['niz_color'] = form.cleaned_data['niz_color']
                if form.cleaned_data['boots']:
                    kwargs['boots'] = form.cleaned_data['boots']
                if form.cleaned_data['boots_color']:
                    kwargs['boots_color'] = form.cleaned_data['boots_color']


                if form.cleaned_data['shramy']:
                    kwargs['shramy'] = form.cleaned_data['shramy']
                if form.cleaned_data['tatu']:
                    kwargs['tatu'] = form.cleaned_data['tatu']
                if form.cleaned_data['protez']:
                    kwargs['protez'] = form.cleaned_data['protez']
                if form.cleaned_data['konech']:
                    kwargs['konech'] = form.cleaned_data['konech']
                posts = Post_user.objects.filter(**kwargs).order_by('-published_date')
                current_page = Paginator(posts, 4)
            else:
                posts = Post_user.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
                current_page = Paginator(posts, 4)
            return render(request, 'blog/post_list_user.html', {'posts': current_page.page(page_number), 'form': form})
    else:
        form = SearchForm1()

    posts = Post_user.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    current_page = Paginator(posts, 4)
    return render(request, 'blog/post_list_user.html', {'posts': current_page.page(page_number), 'form': form})


def post_map(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/map.html', {'post': post})


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
def post_new_user(request):
    if request.method == "POST":
        form = PostFormUser(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.name and not post.surname and not post.fam:
                post.name = 'Имя неизвестно'
            post.save()
            return redirect('app.views.post_detail_user', pk=post.pk)
    else:
        form = PostFormUser()
    return render(request, 'blog/post_edit_user.html', {'form': form})

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
def post_edit_user(request, pk):
    post = get_object_or_404(Post_user, pk=pk)
    if request.method == "POST":
        form = PostFormUser(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.name and not post.surname and not post.fam:
                post.name = 'Имя неизвестно'
            post.published_date = timezone.now()
            post.save()
            return redirect('app.views.post_detail_user', pk=post.pk)
    else:
        form = PostFormUser(instance=post)
    return render(request, 'blog/post_edit_user.html', {'form': form})


@login_required
def post_draft_list(request, page_number=1):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    current_page = Paginator(posts, 4)
    return render(request, 'blog/post_draft_list.html', {'posts': current_page.page(page_number)})


@login_required
def post_draft_list_user(request, page_number=1):
    posts = Post_user.objects.filter(published_date__isnull=True).order_by('created_date')
    current_page = Paginator(posts, 4)
    return render(request, 'blog/post_draft_list_user.html', {'posts': current_page.page(page_number)})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('app.views.post_detail', pk=pk)


@login_required
def post_publish_user(request, pk):
    post = get_object_or_404(Post_user, pk=pk)
    post.publish()
    return redirect('app.views.post_detail_user', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('app.views.post_list')


@login_required
def post_remove_user(request, pk):
    post = get_object_or_404(Post_user, pk=pk)
    post.delete()
    return redirect('app.views.post_list_user')


def post_detail(request, pk):
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
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


def post_detail_user(request, pk):
    post = get_object_or_404(Post_user, pk=pk)
    if request.method == "POST":
        form = CommentFormUser(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = auth.get_user(request).username
            comment.save()
            return redirect('app.views.post_detail_user', pk=post.pk)
    else:
        form = CommentFormUser()
    return render(request, 'blog/post_detail_user.html', {'post': post, 'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('app.views.post_detail', pk=comment.post.pk)


@login_required
def comment_approve_user(request, pk):
    comment = get_object_or_404(Comment_user, pk=pk)
    comment.approve()
    return redirect('app.views.post_detail_user', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('app.views.post_detail', pk=post_pk)


@login_required
def comment_remove_user(request, pk):
    comment = get_object_or_404(Comment_user, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('app.views.post_detail_user', pk=post_pk)


# @login_required
# def comment_edit(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     post = get_object_or_404(Post, pk=pk)
#     comment.delete()
#     return redirect('app.views.post_detail', pk=post_pk, text=comment_text)


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


@login_required
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
    return render(request, 'blog/user_profile.html', args)

