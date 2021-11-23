from instapy import InstaPy
from instapy import smart_run
import schedule
import time

username = 'isorter_machine'
password = 'sorter@123'

hashTags = open('tags.txt').read().splitlines()
accounts = open('accounts.txt').read().splitlines()

# def job():

session = InstaPy(username, password, headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(
        enabled=True, delimit_by_numbers=True, min_followers=50, min_following=50)
    session.set_do_follow(True, percentage=10)

# session.set_dont_like()
# session.follow_by_tags(hashTags)
session.like_by_tags(hashTags, amount=10)
# usersList = session.target_list('accounts.txt')
# session.follow_by_list(usersList, times=1, sleep_delay=600)


# schedule.every().day.at("6:00").do(job)
# schedule.every().day.at("6:00").do(job)
# schedule.every().minute.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
