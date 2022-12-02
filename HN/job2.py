import http.client
import json

from HN.models import PolloptModel, PollModel, CommentModel, JobModel, StoryModel

# max item
current_max_item_id = None

# connection made here
# connect to site
conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")
payload = "{}"


# request starts here

# get item from api
def get_item_id(value):
    return f"/v0/item/{value}.json?print=pretty"


def get_item(url):
    """
    args:
        url(str): url retrieved from id passed to get_item_id
    returns:
        dataArray(str)
    """
    print("\n")
    conn.request("GET", url, payload)
    response = conn.getresponse()
    my_data = response.read()
    data_array = my_data.decode("utf-8")
    return data_array




def job_to_db(dat_id, types, deleted, by, time, dead, kids, text, url, title):
    """Function that passes data to Job Model db"""

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

def story_to_db(dat_id, types, deleted, by, time, dead, kids, descendants, score, title):
    """Function that passes data to Story Model db"""

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

def comment_to_db(dat_id, types, deleted, by, time, dead, kids, parent, text):
    """Function that passes data to Comment Model db"""

    comment_model = CommentModel(
        type=types,
        deleted=deleted,
        by=by,
        time=time,
        dead=dead,
        kids=kids,
        parent=parent,
        text=text
    )

    comment_model.id = dat_id
    comment_model.save()

def poll_to_db(dat_id, types, deleted, by, time, dead, kids, parent, text, parts):
    """Function that passes data to Poll Model db"""

    poll_model = PollModel(
        type=types,
        deleted=deleted,
        by=by,
        time=time,
        dead=dead,
        kids=kids,
        parent=parent,
        text=text,
        parts=parts,
    )

    poll_model.id = dat_id
    poll_model.save()

def pollopt_to_db(dat_id, types, deleted, by, time, dead, kids, parent, score):
    """Function that passes data to Pollopt Model db"""
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


def add_to_db(my_dict):
    """Gets data from dictionary then passes that data to callables"""
    types = my_dict.get('type')
    dat_id = my_dict.get('id')
    deleted = my_dict.get('deleted')
    by = my_dict.get('by')
    time = my_dict.get('time')
    dead = my_dict.get('dead')
    kids = my_dict.get('kids')
    parent = my_dict.get('parent')
    url = my_dict.get('url')
    score = my_dict.get('score')
    descendants = my_dict.get('descendants')
    title = my_dict.get('title')
    text = my_dict.get('text')
    parts = my_dict.get('parts')
    if types == 'job':
        job_to_db(dat_id, types, deleted, by, time, dead, kids, text, url, title)
    if types == 'story':
        story_to_db(dat_id, types, deleted, by, time, dead, kids, descendants, score, title)
    if types == 'comment':
        comment_to_db(dat_id, types, deleted, by, time, dead, kids, parent, text)
    if types == 'poll':
        poll_to_db(dat_id, types, deleted, by, time, dead, kids, parent, text)
    if types == 'pollopt':
        pollopt_to_db(dat_id, types, deleted, by, time, dead, kids, parent, score)
    else:
        return None


def top100():
    """gets the first top 100 elements after which it gets only the differential of the most recent update"""

    global current_max_item_id  # instantiate current max item
    conn.request("GET", "/v0/maxitem.json?print=pretty", payload)
    res = conn.getresponse()
    data = res.read()
    print(f'current max item: {data}')

    dataArray = data.decode("utf-8")


    data_list = (dataArray.replace('[', '').replace(']', '').replace('\n', '').split(
        ','))  # remove [ ] and \n from the string and convert it to a list

    data_list = [c.lstrip().rstrip() for c in data_list]  # strip of preceeding and succeeding whitespaces
    print("\ndata_list after cleaning:")
    print(data_list)
    max_item_id = int(data_list[0]) # new max item id


    if current_max_item_id is None:
        # top_items_list = [i for i in range(max_item_id - 99, max_item_id + 1)]
        # or
        print("First time db loading")
        top_items_list = [i for i in range(int(max_item_id), int(max_item_id) - 100, -1)]  # get the latest 100 item ids first
        current_max_item_id = max_item_id  # set current_max_item for first time
        print('\nTotal items:', len(top_items_list))
        return top_items_list
    else:
        top_items_list = [i for i in range(max_item_id, current_max_item_id, -1)] # get the latest items
        current_max_item_id = max_item_id  # set current_max_item
        print('\nTotal items:', len(top_items_list))
        return top_items_list




def check_item(data:list):
    """ my custom algorithm for transversing the entire length of an item-node"""
    for item in data:
        print(f'\n{item}')
        id_ = get_item_id(item)  # retrieve first id
        content = (get_item(id_))  # get content as str
        content_dict = json.loads(content)  # use json module to convert str to dict
        kids = content_dict.get('kids')
        if kids is not None:
            print(f'item has {len(kids)} kids')
            check_item(kids)
        else:
            print('item has no kids')
            add_to_db(content_dict)
    return None



# loads the db with even child nodes.
def load_db():
    """function for loading data into db"""
    data_list = top100()
    check_item(data_list)
    return None

# loads the db with only top level node
def load_db1():
    """function for loading data into db"""
    data_list = top100()
    for item in data_list:
        print(f'\n{item}')
        id_ = get_item_id(item)  # retrieve first id
        content = (get_item(id_))  # get content as str
        content_dict = json.loads(content)
        add_to_db(content_dict)
    return None