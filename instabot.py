import requests
BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = '**********'

url = BASE_URL + 'users/self/?access_token=%s' % ACCESS_TOKEN
print "URL:"+url
user_info = requests.get(url).json()
print user_info
