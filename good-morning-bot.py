#secret weapon for obtaining id's of everyone 
#in the disguise of cute love bot 

from fbchat import Client
from fbchat.models import *
import random 

client = Client("email", "password")
thread_id = "id"
thread_type = ThreadType.USER

#users = client.searchForUsers("xxx")
#for user in users:
# if user.url == "https://www.facebook.com/xxxxx":
#   print user.uid

if not client.isLoggedIn():
  client.login("email", "password")

words = ["my love", "beatiful", "my dear"]

messageText = "Good morning " + words[random.randint(0, 3)]

client.send(
  Message(text = messageText),
  thread_id = thread_id, 
  thread_type = thread_type) 

client.send(
    Message(text = "❤🧡💛💚💙💜🤍💕💞💓💗💖💘"[random.randint(0,12)]),
    thread_id = thread_id,
    thread_type = thread_type)
