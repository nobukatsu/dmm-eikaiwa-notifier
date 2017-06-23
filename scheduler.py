from apscheduler.schedulers.blocking import BlockingScheduler
import teacher_scraper

sched = BlockingScheduler()
sched.add_job(teacher_scraper.scrape, trigger="interval", minutes=3)
sched.start()
