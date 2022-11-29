from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import SearchForm
from .job import get_item, new_stories, get_max_item
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
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = BaseModel.objects.annotate(
                search=SearchVector('title', 'text', 'by'), ).filter(search=query)
    return render(request, 'searchp.html', {'form': form, 'query': query, 'results': results})


# saves data to the db
max_item_url = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"


def load_db(url):
    max_item_id = get_max_item(url)  # get the current max item
    print(max_item_id)
    id_data_list = [i for i in range(int(max_item_id), int(max_item_id) - 100, -1)]  # get the latest 100 item ids first
    print('first time: ', id_data_list)
    global current_max_item_id
    current_max_item_id = int(max_item_id)

    for data_id in id_data_list:
        my_dict = get_item(data_id)

        types = my_dict.get('type')
        dat_id = my_dict.get('id')
        deleted = my_dict.get('deleted')
        print(deleted)
        by = my_dict.get('by')
        print(f'by: {by}')
        time = my_dict.get('time')
        print(f'time: {time}')
        dead = my_dict.get('dead')
        print(f'dead: {dead}')
        kids = my_dict.get('kids')
        print(f'kids: {kids}')
        parent = my_dict.get('parent')
        print(f'parent: {parent}')
        text = my_dict.get('text')
        print(f'text: {text}')
        url = my_dict.get('url')
        print(f'url: {url}')
        descendants = my_dict.get('descendants')
        print(f'descendants: {descendants}')
        score = my_dict.get('score')
        print(f'score :{score}')
        title = my_dict.get('title')
        print(f'title: {title}')
        parts = my_dict.get('parts')
        print(f'parts: {parts}')

        if types == 'job':
            job_model = JobModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                text=text,
                url=url,
                title=title
            )

            job_model.id = dat_id
            job_model.save()

        if types == 'story':
            story_model = StoryModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                descendants=descendants,
                score=score,
                title=title
            )

            story_model.id = dat_id
            story_model.save()

        if types == 'comment':
            comment_type = CommentModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                parent=parent,
                text=text
            )

            comment_type.id = dat_id
            comment_type.save()

        if types == 'poll':
            poll_model = PollModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                parent=parent,
                text=text,
                descendants=descendants,
                score=score,
                title=title,
                parts=parts
            )

            poll_model.id = dat_id
            poll_model.save()

        if types == 'pollopt':
            pollopt_model = PolloptModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                parent=parent,
                score=score
            )

            pollopt_model.id = dat_id
            pollopt_model.save()


def load_db_after(url):
    #   gets the new stories
    max_item_id = get_max_item(url)  # get the current max item
    print(max_item_id)
    id_data_list = [i for i in range(int(max_item_id), int(max_item_id) - 100, -1)]  # get the latest 100 item ids first
    print('reoccurring time: ', id_data_list)
    global current_max_item_id
    current_max_item_id = int(max_item_id)
    new_items_list_id = id_data_list[:id_data_list.index(current_max_item_id)]  # get the latest 100 item ids
    print('reoccurring times: ', id_data_list)

    for data_id in new_items_list_id:
        my_dict = get_item(data_id)

        types = my_dict.get('type')
        dat_id = my_dict.get('id')
        deleted = my_dict.get('deleted')
        print(deleted)
        by = my_dict.get('by')
        print(f'by: {by}')
        time = my_dict.get('time')
        print(f'time: {time}')
        dead = my_dict.get('dead')
        print(f'dead: {dead}')
        kids = my_dict.get('kids')
        print(f'kids: {kids}')
        parent = my_dict.get('parent')
        print(f'parent: {parent}')
        text = my_dict.get('text')
        print(f'text: {text}')
        url = my_dict.get('url')
        print(f'url: {url}')
        descendants = my_dict.get('descendants')
        print(f'descendants: {descendants}')
        score = my_dict.get('score')
        print(f'score :{score}')
        title = my_dict.get('title')
        print(f'title: {title}')
        parts = my_dict.get('parts')
        print(f'parts: {parts}')

        if types == 'job':
            job_model = JobModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                text=text,
                url=url,
                title=title
            )

            job_model.id = dat_id
            job_model.save()

        if types == 'story':
            story_model = StoryModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                descendants=descendants,
                score=score,
                title=title
            )

            story_model.id = dat_id
            story_model.save()

        if types == 'comment':
            comment_type = CommentModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                parent=parent,
                text=text
            )

            comment_type.id = dat_id
            comment_type.save()

        if types == 'poll':
            poll_model = PollModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                parent=parent,
                text=text,
                descendants=descendants,
                score=score,
                title=title,
                parts=parts
            )

            poll_model.id = dat_id
            poll_model.save()

        if types == 'pollopt':
            pollopt_model = PolloptModel(
                type=types,
                deleted=deleted,
                by=by,
                time=time,
                dead=dead,
                kids=kids,
                parent=parent,
                score=score
            )

            pollopt_model.id = dat_id
            pollopt_model.save()


new_stories_url = '/v0/newstories.json?print=pretty'


def index(request):
    return HttpResponse('<h1>This is a H1 heading!</h1>')


def loadView(request, url: new_stories_url):
    """newest stories are loaded here initially using this route"""

    load_db(url)
    return HttpResponse('<h1>DONE</h1>')

# base_model.deleted = deleted
# base_model.by = by
# base_model.time = time
# base_model.dead = dead
# base_model.kids = kids
# base_model.parent = parent
# base_model.text = text
# base_model.url = url
# base_model.descendants = descendants
# base_model.score = score
# base_model.title = title
# base_model.parts = parts
#
# print('created')
# base_model.save()
# print('saved')

# BaseModel.objects.create(
#     id=my_dict['id'],
#     deleted=my_dict['id'],
#     type=my_dict['type'],
#     by=my_dict['by'],
#     time=my_dict['time'],
#     dead=my_dict.get('dead'),
#     kids=my_dict.get('kids'),  # my_dict['kids'],
#     parent=my_dict['parent'],
#     text=my_dict['text'],
#     url=my_dict['url'],
#     descendants=my_dict['descendants'],
#     store=my_dict['store'],
#     title=my_dict['title'],
#     parts=my_dict['parts']
# )


# deleted=my_dict.get('deleted'),
# type=my_dict.get('type'),
# by=my_dict.get('by'),
# time=my_dict.get('time'),
# dead=my_dict.get('dead'),
# kids=my_dict.get('kids'),
# parent=my_dict.get('parent'),
# text=my_dict.get('text'),
# url=my_dict.get('url'),
# descendants=my_dict.get('descendants'),
# score=my_dict.get('score'),
# title=my_dict.get('title'),
# parts=my_dict.get('parts'),
