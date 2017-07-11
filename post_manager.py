import requests, urllib
import os
from mytoken import ACCESS_TOKEN
BASE_URL = "https://api.instagram.com/v1/"


def get_self_post():
    url = BASE_URL + "users/self/media/recent/?access_token="+ ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "No Recent Post exist"
            return -1
    else:
        print "Status code other than 200 received!"
        return -1

def get_media_liked():
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
            return -1
    else:
        print "Error" + self_media["meta"]["code"]
        return -1

def get_other_post(user_id):
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "No Recent Post exist"
            return -1
    else:
        print "Error" + self_media["meta"]["code"]
        return -1

def get_all_media(user_id,criteria,value):
    ID=[]
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + ACCESS_TOKEN
    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        for media in user_media["data"]:
            if criteria == "1":
                if media["likes"]["count"]>=int(value):
                    ID.append(media["id"])
                    urllib.urlretrieve(media["images"]["standard_resolution"]["url"], media["id"] + ".jpeg")
            else:
                if str(media["caption"]).find(value) != -1:
                    ID.append(media["id"])
                    urllib.urlretrieve(media["images"]["standard_resolution"]["url"], media["id"] + ".jpeg")
        print "Name of downloaded images"
        for id in ID:
            print str(id)+".jpg"

    else:
        print "Error" + user_media["meta"]["code"]
        return -1


def get_other_post_by_criteria(user_id):
    print "1.Get post by min no of likes"
    print "2.Get post by text in caption"
    criteria=raw_input("")
    if criteria == "1":
        value=raw_input("Enter minimum no of likes: ")
        get_all_media(user_id,criteria,value)
    elif criteria == "2":
        value=raw_input("Enter text: ")
        get_all_media(user_id, criteria,value)
