import instaloader
from datetime import datetime
import os

class GetInstaPosts():

    def __init__(self):
        self.L = instaloader.Instaloader()
        self.L.save_metadata = False
        self.L.post_metadata_txt_pattern = ''

    '''
    Gets all the posts on a specific date from a given user's profile.

    Parameters:
    username(str): The username of the profile to get the posts from.
    date(datetime): The datetime object of the date of when to get the posts from.

    Returns:
    list: A list of elements representing in the following order - caption of post, a list of the media posted
    '''

    def get_media(self, username, date):
        profile = instaloader.Profile.from_username(self.L.context, username)
        posts = profile.get_posts()

        new_posts = [post for post in posts if datetime.strftime(post.date, '%Y-%m-%d') == datetime.strftime(date, '%Y-%m-%d')]

        list_posts = []

        for post in new_posts:
            date = datetime.strftime(post.date, '%Y-%m-%d')
            folder_name = r"C:\Users\r4che\Downloads\tweet-poster-alt\posts\New Post " + date
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            self.L.dirname_pattern = folder_name

            self.L.download_post(post, target=folder_name)

            if len(post.caption) > 250:
                caption = input("Please input a suitable caption below 250 characters")
                caption = caption.replace("\\n\\n", "\n\n")
            else:
                caption = post.caption

            data = [caption]

            media = []

            if post.typename == 'GraphSidecar':
                for i in range(post.mediacount):
                    file_name = str(post.date_utc).replace(":", "-").replace(" ", "_") + '_UTC_' + f'{i+1}' + '.jpg'
                    media.append(file_name)
            else:
                media.append(self.L.format_filename(post, target=profile.username) + '.jpg')
            data.append(media)
            list_posts.append(data)

        return list_posts
