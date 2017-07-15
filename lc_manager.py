import requests
from mytoken import ACCESS_TOKEN
from id_manager import get_post_id, get_comment_id
BASE_URL = "https://api.instagram.com/v1/"

def like_recent_post(username):
    media_id = get_post_id(username)
    if media_id == -1:
        return -1
    url = BASE_URL + "media/" + media_id+ "/likes"
    payload = {"access_token": ACCESS_TOKEN}
    post_a_like = requests.post(url, payload).json()
    if post_a_like["meta"]["code"] == 200:
        print "Like successful"
    else:
        print "Like failed"
        print "Error" + str(post_a_like["meta"]["code"])

def get_comment_list(username):
    media_id = get_post_id(username)
    if media_id == -1:
        return -1
    url = BASE_URL + "media/" + media_id + "/comments?access_token=" + ACCESS_TOKEN
    user_media = requests.get(url).json()
    if user_media["meta"]["code"] == 200:
        s_no=1
        for comment in user_media["data"]:
            print str(s_no) + "."+comment["text"]
            s_no+=1
        if s_no == 1:
            print "No Comments Found"
    else:
        print "Error" + str(user_media["meta"]["code"])

def post_comment(username):
    media_id = get_post_id(username)
    if media_id == -1:
        return -1
    comment = raw_input("Your comment: ")
    payload = {"access_token": ACCESS_TOKEN, "text": comment}
    url = BASE_URL + "media/" + media_id + "/comments"
    make_comment = requests.post(url, payload).json()
    if make_comment['meta']['code'] == 200:
        print "Added a new comment"
    else:
        print "Comment failed"
        print "Error" + str(make_comment["meta"]["code"])

def delete_comment(username):
    media_id = get_post_id(username)
    if media_id == -1:
        return -1
    id=get_comment_id(media_id)
    if id.__len__() ==0 :
        print "No comments found"
        return -1
    for comment_id in id:
        print str(comment_id)
        url = BASE_URL + "media/" + media_id + "/comments/"+comment_id+"?access_token=" + ACCESS_TOKEN
        del_comment = requests.delete(url).json()
    if del_comment["meta"]["code"] ==200:
        print "Comment Deleted"
    else:
        print "Error "+str(del_comment["meta"]["code"])