from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import SearchForm
from .job2 import load_db
from .models import *

# Create your views here.
current_max_item_id = None


def post_list(request):
    object_list = BaseModel.objects.all()
    paginator = Paginator(object_list, 15)  # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page': page, 'posts': posts})


def post_list_story(request):
    object_list = StoryModel.objects.all()
    paginator = Paginator(object_list, 15)  # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page': page, 'posts': posts})


def post_list_job(request, ):
    object_list = JobModel.objects.all()
    paginator = Paginator(object_list, 15)  # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page': page, 'posts': posts})


def post_list_comment(request):
    object_list = CommentModel.objects.all()
    paginator = Paginator(object_list, 15)  # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page': page, 'posts': posts})


def post_list_poll(request):
    object_list = PollModel.objects.all()
    paginator = Paginator(object_list, 15)  # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page': page, 'posts': posts})


def post_list_pollopt(request):
    object_list = PolloptModel.objects.all()
    paginator = Paginator(object_list, 15)  # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page': page, 'posts': posts})


def post_detail(request, id):
    global specific_comments
    post = get_object_or_404(BaseModel, id=id)
    if post.type == 'story':
        post = StoryModel.objects.get(id=id)

        comments_list = CommentModel.objects.all()
        specific_comments = []
        for comment in comments_list:
            if comment.parent == post.id:
                specific_comments += [comment]
    if post.type == 'job':
        post = JobModel.objects.get(id=id)

        comments_list = CommentModel.objects.all()
        specific_comments = []
        for comment in comments_list:
            if comment.parent == post.id:
                specific_comments += [comment]
    if post.type == 'comment':
        post = CommentModel.objects.get(id=id)

        comments_list = CommentModel.objects.all()
        specific_comments = []
        for comment in comments_list:
            if comment.parent == post.id:
                specific_comments += [comment]

    return render(request,
                  'hack/detail.html',
                  {'post': post,
                   'comments': specific_comments})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = BaseModel.objects.annotate(
                search=SearchVector('commentmodel', 'by','jobmodel', 'storymodel'), ).filter(search=query)
    return render(request, 'searchp.html', {'form': form, 'query': query, 'results': results})


def index(request):
    return HttpResponse('<h1>This is a H1 heading!</h1>')

