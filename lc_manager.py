import requests, urllib
from token import ACCESS_TOKEN
from id_manager import get_post_id
BASE_URL = "https://api.instagram.com/v1/"

def get_media_likes():
    url = BASE_URL + "users/self/media/liked/?access_token=" + ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "No Recent liked Media found"
            return 0
    else:
        print "Error" + self_media["meta"]["code"]
        return 0

def like_a_post(username):
    media_id = get_post_id(username)
    if media_id==None:
        return
    url = BASE_URL + "media/" + media_id+ "/likes"
    payload = {"access_token": ACCESS_TOKEN}
    post_a_like = requests.post(url, payload).json()
    if post_a_like["meta"]["code"] == 200:
        print "Like successful"
    else:
        print "Like unsuccessful"

def get_comment_list(username):
    media_id = get_post_id(username)
    url = BASE_URL + "media/" + media_id + "/comments?access_token="+ACCESS_TOKEN
    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        for comment in user_media["data"]:
            print comment["text"]+"\n"
    else:
        print "Error"

def post_a_comment(username):
    media_id = get_post_id(username)
    comment = raw_input("Your comment: ")
    payload = {"access_token": ACCESS_TOKEN, "text" : comment}
    url = BASE_URL + "media/"+media_id+"/comments"
    make_comment = requests.post(url, payload).json()
    if make_comment['meta']['code'] == 200:
        print "added a new comment!"
    else:
        print "Failed"