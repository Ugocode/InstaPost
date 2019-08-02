from instapy_cli import client
# remember to first pip install instapy




username = 'ugobozz1'
password = 'Ugomartins1'
image = 'rangeR.png'
text = 'Bought a new baby' + '\r\n   #Python #computer'


with client(username, password) as cli: cli.upload(image, text)



# To automate your instagram to have likes, comment, and follow

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time

#your login credentials
insta_username='ugobozz1'
insta_password='Ugomartins1'

#path to your workspace
set_workspace(path=None)

def job():
  session = InstaPy(username=insta_username, password=insta_password)
  with smart_run(session):
    session.set_do_comment(enabled=True, percentage=20)
    session.set_comments(['Well done!'])
    session.set_do_follow(enabled=True, percentage=5, times=2)
    session.like_by_tags(['love'], amount=50, media='image')


# schedule.every().day.at("7:00").do(job)
# schedule.every().day.at("16:22").do(job)

# while True:
#   schedule.run_pending()
#   time.sleep(10)
