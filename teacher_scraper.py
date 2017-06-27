import requests
from bs4 import BeautifulSoup

BASE_URL = "http://eikaiwa.dmm.com/teacher/index/"


def scrape():
    ids = get_target_ids()
    
    for id_ in ids:
        teacher_url = BASE_URL + id_ + "/"
        
        res = requests.get(teacher_url)
        soup = BeautifulSoup(res.content, "lxml")

        teacher_name = get_teacher_name(soup)

        schedule_list = soup.find("div", class_="schedules-list")
        today = schedule_list.find("ul", class_="oneday")

        print("id: " + id_)
        print("name: " + teacher_name)
        print(today)


def get_target_ids():
    return ["4137"]


def get_teacher_name(soup):
    teacher_name = soup.find("h1")
    return teacher_name.get_text()


if __name__ == "__main__":
    scrape()
