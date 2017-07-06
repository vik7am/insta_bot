import requests, urllib
from token import ACCESS_TOKEN

BASE_URL = 'https://api.instagram.com/v1/'

def get_self_info():
    url = BASE_URL + "users/self/?access_token=" + ACCESS_TOKEN
    print "URL: "+url
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
    #print "URL:"+url
    user_info = requests.get(url).json()
    #print user_info
    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            return user_info["data"][0]["id"]
        else:
            return "User not Found"
    else:
        print "Error"+user_info["meta"]["code"]

def get_self_post():
    url = BASE_URL + "users/self/media/recent/?access_token="+ ACCESS_TOKEN
    print "URL:" + url
    own_media = requests.get(url).json()
    s_no=1
    for media in own_media["data"]:
        caption = "No Caption"
        if media["caption"] != None:
            caption = media["caption"]["text"]
        print str(s_no) + ". " + media["id"] + " " + str(caption)
        s_no += 1

def get_other_post(user_id):
    url = BASE_URL + "users/"+user_id+"/media/recent/?access_token="+ ACCESS_TOKEN
    print "URL:" + url
    own_media = requests.get(url).json()
    s_no=1
    for media in own_media["data"]:
        caption="No Caption"
        if media["caption"]!=None:
            caption = media["caption"]["text"]
        print str(s_no)+". "+media["id"]+" "+str(caption)
        s_no+=1

def home():
    running=True
    while running:
        print "1.Get Self info "
        print "2.Get Other User ID"
        print "3.Get Self Post"
        print "4.Get Other Post"
        choice=raw_input("")
        if choice=="1":
            get_self_info()
        elif choice=="2":
            user=raw_input("Enter Username:")
            print str(get_user_id(user))
        elif choice=="3":
            get_self_post()
        elif choice=="4":
            get_other_post(get_user_id("instabot.mriu.test.8"))
        else:
            running=False
        print "\n"

home()