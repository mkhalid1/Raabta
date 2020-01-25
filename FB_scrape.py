#!/usr/bin/env python
# coding: utf-8

from facebook_scraper import get_posts
# For Groups

count = 0
group_posts = []

for post in get_posts(group= 1259852177422636, credentials= (),pages=1):
    group_posts.append(post)
    count+=1

print("Posts Extracted: ", count)
print("\n\nPost #1", group_posts[0])

## Structure of a post

# {'post_id': '2257188721032235',
#  'text': 'Don’t let this diminutive version of the Hero of Time fool you, '
#          'Young Link is just as heroic as his fully grown version! Young Link '
#          'joins the Super Smash Bros. series of amiibo figures!',
#  'time': datetime.datetime(2019, 4, 29, 12, 0, 1),
#  'image': 'https://scontent.flim16-1.fna.fbcdn.net'
#           '/v/t1.0-0/cp0/e15/q65/p320x320'
#           '/58680860_2257182054366235_1985558733786185728_n.jpg'
#           '?_nc_cat=1&_nc_ht=scontent.flim16-1.fna'
#           '&oh=31b0ba32ec7886e95a5478c479ba1d38&oe=5D6CDEE4',
#  'likes': 2036,
#  'comments': 214,
#  'shares': 0,
#  'post_url': 'https://m.facebook.com/story.php'
#              '?story_fbid=2257188721032235&id=119240841493711',
#  'link': 'https://bit.ly/something'}


# For Pages


count = 0
page_posts = []

for post in get_posts('AlImdaadFoundationUK', credentials = (), pages=1):

	page_posts.append(post)
	count+=1

print("\n\nPosts Extracted: ", count)
print("\n\nPost #1",page_posts[0])
