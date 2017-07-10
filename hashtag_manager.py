import requests
from token import ACCESS_TOKEN
from id_manager import get_user_id
BASE_URL = "https://api.instagram.com/v1/"

HASHTAG=[]
CAPTION=[]
def find_hashtag(user_id):
    counter=0
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + ACCESS_TOKEN
    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        #length=len(user_media["data"])
        for media in user_media["data"]:
            caption=media["caption"]["text"]
            CAPTION.append(caption)

        for caption in CAPTION:
            WORD=str(caption).split(" ")
            for word in WORD:
                if str(word).find("#") != -1:
                    if find_duplicates(word):
                        HASHTAG.append(word)


        sno=1
        for h in HASHTAG:
            print str(sno)+h
            sno+=1
        return counter
    else:
        print "Error" + user_media["meta"]["code"]
        return -1

def find_duplicates(word):
    for hashtag in HASHTAG:
        if hashtag == word:
            return False
    return True





def get_image_with_hashtag(username):
    user_id=get_user_id(username)
    find_hashtag(user_id)
    #print "No of images with "+hashtag+" : "+str(no_of_images)