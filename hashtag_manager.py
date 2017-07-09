import requests
from token import ACCESS_TOKEN
from id_manager import get_user_id
BASE_URL = "https://api.instagram.com/v1/"

def find_hashtag(user_id,hashtag):
    counter=0
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        for media in self_media["data"]:
            caption=media["caption"]["text"]
            if str(caption).find(hashtag)>=0:
                counter+=1
        return counter
    else:
        print "Error" + self_media["meta"]["code"]
        return -1

def get_image_with_hashtag(username,hashtag):
    user_id=get_user_id(username)
    no_of_images=find_hashtag(user_id,hashtag)
    print "No of images with "+hashtag+" : "+str(no_of_images)