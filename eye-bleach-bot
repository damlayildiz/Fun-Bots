import praw
from twilio.rest import Client


reddit = praw.Reddit(client_id= "client_id",
                     client_secret="client_secret",
                     user_agent="user_agent",
                     username="	username",
                     password="password")

def main():
    posts = reddit.subreddit("eyebleach").top("day")
    post_urls = []
    for post in posts:
        post_urls.append("https://www.reddit.com" + post.permalink)
    post_urls = post_urls[:3]

    account_sid = 'account_sid'
    auth_token = 'auth_token'
    client = Client(account_sid, auth_token)

    text = ""

    for link in post_urls:
        text += "*"
        text += link
        text += "\n"

    message = client.messages \
        .create(
        body="t",
        from_='+12562075022',
        to='+905348664601'
    )

    if (message.error_message != None or message.error_message != "None"):
        main()

if __name__ == "__main__":
    main()
