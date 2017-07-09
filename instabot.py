import requests, urllib
from token import ACCESS_TOKEN

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
            print "Incorrect Username"
    else:
        print "Error: "+self_info["meta"]["code"]

def get_user_id(username):
    url = BASE_URL + "users/search?q="+username+"&access_token=" +ACCESS_TOKEN
    user_info = requests.get(url).json()

    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            return user_info["data"][0]["id"]
        else:
            return "User not Found"
    else:
        print "Error"+user_info["meta"]["code"]

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
            print "Post does not exist!"
            return 0
    else:
        print "Status code other than 200 received!"
        return 0
    

def get_other_post(user_id):
    url = BASE_URL + "users/"+user_id+"/media/recent/?access_token="+ ACCESS_TOKEN
    self_media = requests.get(url).json()

    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "Post does not exist!"
            return 0
    else:
        print "Error" + self_media["meta"]["code"]
        return 0

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

def get_post_id(username):
    user_id = get_user_id(username)
    if user_id == None:
        print "User does not exist!"
        return None
    url = BASE_URL + "users/"+user_id+"/media/recent/?access_token="+ ACCESS_TOKEN

    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            return user_media["data"][0]["id"]
        else:
            print "No Recent liked Media found"
            return None
    else:
        print "Error" + user_media["meta"]["code"]
        return None

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


def home():
    running=True

    while running:
        print "1.Get Self info "
        print "2.Get Other User ID"
        print "3.Get Self Post"
        print "4.Get Other Post"
        print "5.Get recent media liked by the user"
        print "6.Like a Post"
        choice=raw_input("")
        if choice=="1":
            get_self_info()
        elif choice=="2":
            user=raw_input("Enter Username:")
            print str(get_user_id(user))
        elif choice=="3":
            image_id=get_self_post()
            print "Downloaded "+str(image_id)+".jpg"
        elif choice=="4":
            user_id=raw_input("Enter UserName: ")
            image_id = get_other_post(get_user_id(user_id))
            print "Downloaded " + str(image_id) + ".jpg"
        elif choice == "5":
            id=get_media_likes()
            print "Downloaded " + str(id) + ".jpg"
        elif choice == "6":
            user_id = raw_input("Enter UserName: ")
            like_a_post(user_id)
        else:
            running=False
        print "\n"

home()