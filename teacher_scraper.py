import requests
from bs4 import BeautifulSoup

BASE_URL = "http://eikaiwa.dmm.com/teacher/index/"

def scrape():
    ids = get_target_ids()
    
    for id in ids:
        teacher_url = BASE_URL + id + "/"
        
        res = requests.get(teacher_url)
        soup = BeautifulSoup(res.content, "html.parser")
        
        sche_list = soup.find("div", class_="schedules-list")
        today = sche_list.find("ul", class_="oneday")
        
        print(today)


def get_target_ids():
    return ["4137"]


if __name__ == "__main__":
    scrape()
