from id_manager import get_self_info,get_user_id
from post_manager import get_self_post,get_other_post,get_media_liked
from lc_manager import like_a_post,get_comment_list,post_a_comment
from hashtag_manager import get_image_with_hashtag
BASE_URL = "https://api.instagram.com/v1/"

def home():
    running=True
    while running:
        print "1.Get Self info "
        print "2.Get Other User ID"
        print "3.Get Self Post"
        print "4.Get Other Post"
        print "5.Get recent media liked by the user"
        print "6.Like a Post"
        print "7.Get List of comments"
        print "8.Comment on a Post"
        print "9.Get no of post with hash tag"
        print "0.Exit"
        choice=raw_input("")
        if choice=="1":
            get_self_info()

        elif choice=="2":
            username=raw_input("Enter Username:")
            user_id= get_user_id(username)
            if user_id !=-1:
                print "User ID of "+username+" : "+str(user_id)

        elif choice=="3":
            image_id=get_self_post()
            if image_id!=-1:
                print "Downloaded "+str(image_id)+".jpg"

        elif choice=="4":
            username=raw_input("Enter UserName: ")
            user_id=get_user_id(username)
            image_id = get_other_post(user_id)
            if image_id != -1:
                print "Downloaded " + str(image_id) + ".jpg"

        elif choice == "5":
            image_id=get_media_liked()
            if image_id != -1:
                print "Downloaded " + str(image_id) + ".jpg"

        elif choice == "6":
            username = raw_input("Enter UserName: ")
            like_a_post(username)

        elif choice == "7":
            username = raw_input("Enter UserName: ")
            get_comment_list(username)

        elif choice == "8":
            username = raw_input("Enter UserName: ")
            post_a_comment(username)

        elif choice == "9":
            username = raw_input("Enter UserName: ")
            #hashtag = raw_input("Enter Hashtag: ")
            get_image_with_hashtag(username)

        else:
            running=False
        print "\n"
home()