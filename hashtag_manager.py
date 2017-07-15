import requests
import matplotlib.pyplot as graph
import numpy
from mytoken import ACCESS_TOKEN
from id_manager import get_user_id
graph.rcdefaults()

BASE_URL = "https://api.instagram.com/v1/"
CAPTION=[]
HASHTAG=[]
NO_OF_IMAGE=[]

def find_hashtag(user_id):
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + ACCESS_TOKEN
    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        for media in user_media["data"]:
            caption=media["caption"]["text"]
            CAPTION.append(caption)
        for caption in CAPTION:
            WORD=str(caption).split(" ")
            for word in WORD:
                if str(word).find("#") == 0:
                    if find_duplicates(word):
                        HASHTAG.append(word)
    else:
        print "Error" + str(user_media["meta"]["code"])

def find_duplicates(word):
    for hashtag in HASHTAG:
        if hashtag == word:
            return False
    return True

def find_images():
    for hashtag in HASHTAG:
        counter=0
        for caption in CAPTION:
            if str(caption).find(hashtag)>=0:
                counter+=1
        NO_OF_IMAGE.append(counter)

def draw_graph():
    Y_AXIS = numpy.arange(len(HASHTAG))
    graph.bar(Y_AXIS, NO_OF_IMAGE, align="center", alpha=0.5)
    graph.xticks(Y_AXIS, HASHTAG)
    graph.ylabel("No of images")
    graph.title("Popular trends on the internet")
    graph.show()

def show_trending_hashtags(username):
    user_id=get_user_id(username)
    find_hashtag(user_id)
    if HASHTAG.__len__() == 0:
        print "No Trending Hashtags"
        return -1
    find_images()
    draw_graph()
