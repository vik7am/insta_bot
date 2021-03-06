from id_manager import get_self_info,get_user_id
from post_manager import get_self_post,get_user_post,get_post_liked,show_user_post_by_criteria
from lc_manager import like_recent_post,get_comment_list,post_comment,delete_comment
from hashtag_manager import show_trending_hashtags
BASE_URL = "https://api.instagram.com/v1/"

def home(username):
    running=True
    while running:
        print "***INSTABOT HOME***"
        print "1.Self info "
        print "2.Recent post"
        print "3.Recent media liked"
        print "4.Like recent post"
        print "5.List of comments on recent post"
        print "6.Make comment on my recent a post"
        print "7.Find trending HashTags"
        print "8.Go to other user profile"
        print "0.Exit"
        choice=raw_input("")
        if choice=="1":
            get_self_info()
        elif choice=="2":
            image_id=get_self_post()
            if image_id!=-1:
                print "Downloaded "+str(image_id)+".jpg"
        elif choice == "3":
            image_id=get_post_liked()
            if image_id != -1:
                print "Downloaded " + str(image_id) + ".jpg"
        elif choice == "4":
            like_recent_post(username)
        elif choice == "5":
            get_comment_list(username)
        elif choice == "6":
            post_comment(username)
        elif choice == "7":
            show_trending_hashtags(username)
        elif choice == "8":
            other_username=raw_input("Enter Username: ")
            other_user_profile(other_username)
        else:
            running=False
        print "\n"

def other_user_profile(username):
    user_id=get_user_id(username)
    if user_id ==-1:
        return -1
    running=True
    while running:
        print "***INSTABOT "+username+" PROFILE***"
        print "1.User ID"
        print "2.Recent post"
        print "3.Posts by criteria"
        print "4.Like recent post"
        print "5.List of comments on recent post"
        print "6.Make comment on recent a post"
        print "7.Delete all comments on recent post"
        print "8.Find trending HashTags"

        print "0.Go to self profile"
        choice=raw_input("")
        if choice == "1":
            print "User ID of "+username+" is "+user_id
        elif choice == "2":
            iamge_id=get_user_post(user_id)
            if iamge_id !=-1:
                print str(iamge_id)+".jpg"+" is downloaded"
        elif choice == "3":
            show_user_post_by_criteria(user_id)
        elif choice == "4":
            like_recent_post(username)
        elif choice == "5":
            get_comment_list(username)
        elif choice == "6":
            post_comment(username)
        elif choice == "7":
            delete_comment(username)
        elif choice == "8":
            show_trending_hashtags(username)
        else:
            running=False
        print "\n"

print "SANDBOX USERNAME = vikrant7am "
print "Welcome vik7am\n"
home("vik7am")