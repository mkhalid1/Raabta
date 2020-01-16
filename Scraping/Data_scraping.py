#!/usr/bin/env python
# coding: utf-8

# In[2]:


import praw  
import pandas as pd  
import numpy as np


# In[3]:


reddit = praw.Reddit(client_id='0rr-7cBdvQvn_A',  
                     client_secret='3TIwcnt2H_jSdJUJtkk2BtuFFvI', 
                     user_agent='Raabta') 


# In[4]:


# get posts from the subreddits related to donations 
hot_post_1 = reddit.subreddit('donate').hot(limit= 5000) 
hot_post_2 = reddit.subreddit('Assistance').hot(limit= 5000) 
hot_post_3 = reddit.subreddit('Charity').hot(limit= 5000) 
hot_post_4 = reddit.subreddit('Donation').hot(limit= 5000) 
hot_post_5 = reddit.subreddit('gofundme').hot(limit= 5000) 
hot_post_6 = reddit.subreddit('RandomKindness').hot(limit= 5000) 


posts = []
for post in hot_post_1:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

for post in hot_post_2:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    
for post in hot_post_3:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

for post in hot_post_4:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    
for post in hot_post_5:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    
for post in hot_post_6:
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
#posts


# In[5]:


df = pd.DataFrame(data=posts)


# In[6]:


dataframe = df.to_csv(r'donations.csv')


# ## Data Processing

# In[7]:


df = pd.read_csv('donations.csv')


# In[8]:


df = df.drop(['id', 'subreddit', 'num_comments', 'url', 'created'],1)


# In[9]:


df = df[['title', 'score','body']]


# In[13]:


print(df.head())


# In[11]:


df.shape


# In[12]:


dataframe = df.to_csv(r'donations.csv')

