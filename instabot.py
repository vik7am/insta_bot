import requests
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
    print "URL:"+url
    user_info = requests.get(url).json()
    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            return user_info["data"][0]["id"]
        else:
            return "User not Found"
    else:
        print "Error"+user_info["meta"]["code"]

get_self_info()
print str(get_user_id("vik7am"))
