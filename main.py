from dotenv import load_dotenv
from get_insta_posts import GetInstaPosts
import os
from datetime import datetime
import tweepy

load_dotenv()

BEARER_TOKEN = os.getenv('bearer_token')
API_KEY = os.getenv('api_key')
API_SECRET = os.getenv('api_secret')
ACCESS_TOKEN = os.getenv('access_token')
ACCESS_TOKEN_SECRET = os.getenv('access_token_secret')

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

insta = GetInstaPosts()

date = datetime(2023, 10, 4)

file_destination = (
        r'C:\Users\r4che\Downloads\tweet-poster-alt\posts\New Post '
        + datetime.strftime(date, '%Y-%m-%d')
        + "\\"
)
print(file_destination)

posts_data = insta.get_media('kclwistem', date)

print(posts_data)

for post in posts_data:
    media_ids = []
    caption = '' if not post[0] else post[0]

    for media in post[1]:
        media_path = file_destination + media
        file_name = file_destination + media
        m = api.media_upload(file_name)
        media_id = m.media_id
        media_ids.append(media_id)
        print(media_ids)

    client.create_tweet(text=caption, media_ids=media_ids, user_auth=True)
