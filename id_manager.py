import requests
from mytoken import ACCESS_TOKEN
BASE_URL = "https://api.instagram.com/v1/"

def get_self_info():
    url = BASE_URL + "users/self/?access_token=" + ACCESS_TOKEN
    self_info = requests.get(url).json()
    if self_info["meta"]["code"] == 200:
        if len(self_info["data"]):
            print "Username: " +self_info["data"]["username"]
            print "Posts: " + str(self_info["data"]["counts"]["media"])
            print "Followers: " +str(self_info["data"]["counts"]["followed_by"])
            print "Following: " +str(self_info["data"]["counts"]["follows"])
        else:
            print "Invalid Username"
    else:
        print "Error: "+str(self_info["meta"]["code"])

def get_user_id(username):
    url = BASE_URL + "users/search?q=" + username + "&access_token=" + ACCESS_TOKEN
    user_info = requests.get(url).json()
    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]) == 1:
            return user_info["data"][0]["id"]
        else:
            print "Invalid user name"
            id=raw_input("enter user id manualy")
            return id
    else:
        print "Error"+str(user_info["meta"]["code"])
        return -1

def get_post_id(username):
    user_id = get_user_id(username)
    if user_id == -1:
        print "User does not exist!"
        return -1
    url = BASE_URL + "users/"+user_id+"/media/recent/?access_token="+ ACCESS_TOKEN
    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            return user_media["data"][0]["id"]
        else:
            print "No Recent liked Media found"
            return -1
    else:
        print "Error" + str(user_media["meta"]["code"])
        return -1