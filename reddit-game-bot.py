import praw
from praw.models import Message
import time

reddit = praw.Reddit(client_id = "client_id",
                     client_secret ="client_secret",
                     user_agent ="user_agent",
                     username ="	username",
                     password ="password")
minute: int = 0
a= True
while a:
    message = "Hi, ov_yoo. I am one of the reddit bots. Everyday I randomly choose some redditor for a little challenge. " \
              "And today the lucky person is you. So here is the game, you will keep getting this message every 10 minute until you find the answer of the question below. " \
              "But to able to find the right answer, you should first decrypt the question. (Don't worry it is commonly used decryption throught the history.)" \
              "And here is the counter to keep you stressed :). Minute:" + str(minute) + \
              "\n\n\nWvkm cxwv i bqum bpmzm eia i bwqtmb qv i akpwwt. " \
              "Emtt ib tmiab qb twwsml tqsm wvm nzwu wcbaqlm." \
              "Jcb ikbcittg qb eia uwzm bpiv rcab i bwqtmb." \
              "Qb eia ikbcittg i xiaaiom jmbemmv xizittmt cvqdmzama." \
              "Abzivom bpqvoa abizbml bw pixxmv epmv bew oqzta lmkqlml bw cam bpib." \
              " Bpmg vwbqkml bpib mdmzgbqum bpmg ow bw bpib bwqtmb," \
              "bpm wvm bpib cam bpm kijqv epqkp kwvbiqva bpm xiaaiom emzmv'b bpm aium xmzawv epw kium wcb wn bpib kijqv." \
              "Bpm mdmvb bpib kicaml bpmu bw acaxmkb nzwu mikp wbpmz eia bpm kpivom qv bpm vium wn bpmqz eitt." \
              "Aw epib eia bpm vium wn bpm eitt inbmz wvm wn bpm oqzta kpivoml cvqdmzama?" \
              "\n\nWhen you think you find the right answer to this question reply this message with just your anwer in all lowercases." \
              "Don't include anyhting other than letters. And don't forget to put just one space between words if there is more than one word in your answer."
    reddit.redditor("ov_yoo").message("GAME", message)
    for item in reddit.inbox.unread(limit=1):
        item.mark_read()
        unread_message = item
        message_body = unread_message.body
        print(message_body)
        if message_body == "xavier":
            a = False
    minute += 10
    print(minute)
    time.sleep(600)

reddit.redditor("ov_yoo").message("GAME", "Congratulations!! It was so much fun for my developer to code me. It took more than one and half hour for me to "\
                                               "be created. So I hope you enjoyed it too. My work is done here so these are my last words. I am vanisihing in the"
                                               " dark corners of the computer. Bye :)")
