#!/usr/bin/python

'''
Checks new posts at a subreddit
Then every 2 minutes it will check to see for new submissions and
send an email if anything is found 

Improvement would be to go by post id or date instead of title since can 
have repeated titles
'''

import praw
import time
import smtplib

# Add your info here
USER_NAME = '' # your reddit username, for example '/u/username'
GMAIL_USER = "" # gmail address, for example name@gmail.com
GMAIL_PWD = "" # gmail password
GMAIL_TO_USER = ''
DELAY_IN_SECONDS_BETWEEN_RUNNING = 120 # default is 120 seconds
client_id = ''

def send_email(text):
    '''
    sends email with given text through gmail
    '''
    FROM = GMAIL_USER
    TO = [GMAIL_TO_USER] #must be a list
    SUBJECT = "New Freebies posts"
    TEXT = text

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PWD)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
                
def run_freebie_bot(current_submissions):
    '''
    the first time it is run it will just return the 50 newest submissions
    the next times it is run it will get 20 newest submissions and look for any ones
    that weren't in the last 50 submissions
    these will be considered 'new' and an email will be sent
    '''
    # to do
        
def check_new_submissions(subreddit_name, number_to_check):
    '''
    for given subreddit, returns the x newest submissions where x = number_to_check
    '''
    # user agent should be unique and descriptive
    r = praw.Reddit(client_id='',
        client_secret='',
        user_agent = 'check new posts by {}'.format(USER_NAME))
     
    submission_list = [submission.title for submission in r.subreddit(subreddit_name).new(limit=number_to_check)]
    return submission_list
    
if __name__ == "__main__":
    current_submissions = []
    while True:
        try:
            current_submissions = run_freebie_bot(current_submissions)
            time.sleep(DELAY_IN_SECONDS_BETWEEN_RUNNING)
	    #print('It worked okay')
        except:
            time.sleep(DELAY_IN_SECONDS_BETWEEN_RUNNING)
            print('Something went wrong so trying again')
    
