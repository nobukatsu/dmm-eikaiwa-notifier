from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from bs4 import BeautifulSoup

URL = "http://eikaiwa.dmm.com/teacher/index/4137/"

html = requests.get(URL)
soup = BeautifulSoup(html, "html.parser")


sched = BlockingScheduler()
@sched.scheduled_job("interval", minutes=3)
def timed_job():
    print("This job is run every three minutes.")
    
sched.start()
