import config as cfg
import praw

reddit = praw.Reddit(client_id=cfg.info['client'],
             	client_secret=cfg.info['secret'],
             	user_agent=cfg.info['useragent'])

with open('scrapdata.txt', 'w', encoding='utf-8') as f:
	for submission in reddit.subreddit('OverwatchUniversity').hot(limit=100):
		f.write(submission.title)
		f.write('\n')
		f.write(submission.selftext)

		submission.comments.replace_more(limit=0)

		for comment in submission.comments.list():
			f.write(comment.body)
			f.write('\n')
		f.write('\n')