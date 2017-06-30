import requests
from bs4 import BeautifulSoup
from datetime import datetime


BASE_URL = "http://eikaiwa.dmm.com/teacher/index/"


def scrape():
    ids = get_target_ids()

    now = datetime.now()
    this_year = now.strftime("%Y")

    # each teacher
    for id_ in ids:
        teacher_url = BASE_URL + id_ + "/"
        
        res = requests.get(teacher_url)
        soup = BeautifulSoup(res.content, "lxml")

        teacher_name = get_teacher_name(soup)

        schedule_list = soup.find("div", class_="schedules-list")
        day_columns = schedule_list.find_all("ul", class_="oneday")

        # each day
        for day_column in day_columns:
            # each time
            for time_row in day_column.find_all("li"):
                print(time_row)

        # target_date = get_schedule_date(day_column.find("li").get_text(), this_year)
        #
        # print("id: " + id_)
        # print("name: " + teacher_name)
        # print(target_date)
        # print(day_columns)


def get_target_ids():
    return ["4137"]


def get_teacher_name(soup):
    teacher_name = soup.find("h1")
    return teacher_name.get_text()


def get_schedule_date(date_str, this_year):

    schedule_date = datetime.strptime(this_year + "-" + date_str[0:2] + "-" + date_str[3:5], "%Y-%m-%d")

    return schedule_date


if __name__ == "__main__":
    scrape()
