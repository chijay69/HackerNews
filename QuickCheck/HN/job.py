import http.client
import json

# connect to site
conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")
payload = "{}"

current_top_story_id = {}  # stores the current_top_story_id
current_new_story_id = {}  # stores the current_new_story_id


# request starts here
# get top stories
def get_item(value):
    # print("\n")
    url = f'/v0/item/{value}.json?print=pretty'
    conn.request("GET", url, payload)
    res = conn.getresponse()
    data = res.read()
    data_array = data.decode("utf-8")  # decode bytes to string

    data_array = json.loads(data_array)
    # data_dict = eval(data_array)
    print(f'data type: {type(data_array)}')
    return data_array


def get_items(url):
    """
    args:
        url(str): url retrieved from id passed to get_item_id
    returns:
        dataArray(str)
    """
    # print("\n")
    conn.request("GET", url, payload)
    res = conn.getresponse()
    data = res.read()
    data_array = data.decode("utf-8")  # decode bytes to string

    # print(f'data type: {type(data)}')
    return data_array


def new_stories(url):
    print("Get new stories id")

    data_array = get_items(url)
    data_list = (data_array.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '').split(
        ','))  # remove [ ] and \n from the string and convert it to a list
    data_list = data_list[:100]
    # print(data_list)
    # print(f'data_list type: {type(data_list)}')
    # print(f'data_array type: {type(data_array)}')

    return data_list


def get_newest_story(url):
    data_list = new_stories(url)
    new_story_id = data_list[0]
    # print(f'new_story_id: {new_story_id}')
    item = get_item(new_story_id)
    current_new_story_id['id'] = item
    # print(new_story_id, item)
    return new_story_id, item


def top_stories(url):
    print("Get top stories id")

    data_array = get_items(url)
    data_list = (data_array.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '').split(
        ','))  # remove [ ], \n and empty spaces from the string and convert it to a list
    data_list = data_list[:100]
    # print(data_list)
    # print(f'data_list type: {type(data_list)}')
    # print(f'data_array type: {type(data_array)}')

    return data_list


def items(url):
    print("Get top stories id")

    data_array = get_items(url)
    data_list = (data_array.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '').split(
        ','))  # remove [ ], \n and empty spaces from the string and convert it to a list
    data_list = data_list[:100]
    print(data_list)
    print(f'data_list type: {type(data_list)}')

    return data_list


def get_top_story(url):
    data_list = top_stories(url)
    top_story_id = data_list[0]
    # print(f'top_story_id: {top_story_id}')
    item = get_item(top_story_id)
    current_top_story_id['id'] = item
    # print(top_story_id, item)
    return top_story_id, item


def loop_dict(url):
    item = get_top_story(url)
    my_dict = json.loads(item)
    key_type = ''
    for key in my_dict:
        print(f'{key} : {my_dict.get(key)}')
        key_type = my_dict.get(key)
    print(key_type)


# saves data to the db
# def load_db(url, myModel):
#     item = get_top_story(url)
#     my_dict = json.loads(item)
#     db_id = my_dict.get('id', None)
#     deleted = my_dict.get('deleted', None)
#     db_type = my_dict.get('type', None)
#     by = my_dict.get('by', None)
#     time = my_dict.get('time', None)
#     dead = my_dict.get('dead', None)
#     kids = my_dict.get('kids', None)
#     parent = my_dict.get('parent', None)
#     text = my_dict.get('text', None)
#     db_url = my_dict.get('url', None)
#     descendants = my_dict.get('descendants', None)
#     score = my_dict.get('score', None)
#     title = my_dict.get('title', None)
#     parts = my_dict.get('parts', None)
#     base_model = myModel.objects.get(id=id)
#     if base_model is None:
#         base_model = myModel(id=db_id, type=db_type)
#         base_model.deleted = deleted
#         base_model.by = by
#         base_model.time = time
#         base_model.dead = dead
#         base_model.kids = kids
#         base_model.parent = parent
#         base_model.db_url = db_url
#         base_model.descendants = descendants
#         base_model.text = text
#         base_model.score = score
#         base_model.title = title
#         base_model.parts = parts
#         base_model.save()


#
# def get_model_save(argument, data):
#     def job(data):
#         for key in data:
#             JobModel.objects.create(
#                 key=data.get(key)
#             )
#         print("Job Model created")
#
#     def story(data):
#         for key in data:
#             StoryModel.objects.create(
#                 key=data.get(key)
#             )
#         print("Story Model created")
#
#     def comment(data):
#         for key in data:
#             CommentModel.objects.create(
#                 key=data.get(key)
#             )
#         print("Comment Model created")
#
#     def poll(data):
#         for key in data:
#             PollModel.objects.create(
#                 key=data.get(key)
#             )
#         print("Poll Model created")
#
#     def pollopt(data):
#         for key in data:
#             PolloptModel.objects.create(
#                 key=data.get(key)
#             )
#         print("Pollopt Model created")
#
#     switcher = {
#         'job': job(data),
#         'story': story(data),
#         'comment': comment(data),
#         'poll': poll(data),
#         'pollopt': pollopt(data)
#     }
#
#     return switcher.get(argument, "Invalid ")
#
#
# # Driver program
# if __name__ == "__main__":
#     print(get_model_save('job'))
#     print(get_model_save('story'))
#     print(get_model_save('poll'))

url = '/v0/newstories.json?print=pretty'

new_stories('/v0/newstories.json?print=pretty')


# top_stories('/v0/newstories.json?print=pretty')
# get_top_story(url)
# loop_dict(url)

def data_list_sample(url, amt):
    sample = new_stories(url)[:amt]
    print(sample)
    return sample


def display_items(url, amt):
    sample = data_list_sample(url, amt)
    for item_id in sample:
        print(get_item(item_id))


max_item_url = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"


def get_max_item(url):
    val = get_items(url)
    print(val)
    return val


# data_list_sample(url)
# display_items(url, 5)

# var = get_top_story(url)

max_id = get_max_item(max_item_url)
print(type(max_id))
my_item = get_item(int(max_id))
# print(my_item['kids'])
print(my_item.get('kids'))
