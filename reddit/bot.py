# Praw
import praw

# General imports
import os

# General setup
subreddit = "BobbbayBots"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
client_password = os.environ.get('client_password')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='The I/O in Io.',
                     username='NexusBot') # TODO: change this username
                     
while 1:
  print("Hello World!")
