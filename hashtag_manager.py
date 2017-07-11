import requests
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from mytoken import ACCESS_TOKEN
from id_manager import get_user_id

BASE_URL = "https://api.instagram.com/v1/"

CAPTION=[]
HASHTAG=[]
IMAGE=[]
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
                if str(word).find("#") != -1:
                    if find_duplicates(word):
                        HASHTAG.append(word)
    else:
        print "Error" + user_media["meta"]["code"]
        return -1

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
        IMAGE.append(counter)

def draw_graph():
    objects = HASHTAG
    y_pos = np.arange(len(objects))
    performance = IMAGE

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('No of images')
    plt.title("Trend analysis")

    plt.show()

def get_image_with_hashtag(username):
    user_id=get_user_id(username)
    find_hashtag(user_id)
    if HASHTAG.__len__() == 0:
        print "No Trending Hashtags"
        return -1
    find_images()
    draw_graph()
    sno = 0
    for h in HASHTAG:
        print str(sno+1) + h + " : " +str(IMAGE[sno])
        sno += 1
