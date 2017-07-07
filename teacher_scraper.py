from datetime import datetime
import requests
from time import sleep
from bs4 import BeautifulSoup
import bookmark
from status import Status

BASE_URL = "http://eikaiwa.dmm.com/teacher/index/"


def scrape():
    ids = __get_target_ids()

    now = datetime.now()
    this_year = now.strftime("%Y")

    # each teacher
    for id_ in ids:
        teacher_url = BASE_URL + id_ + "/"
        
        res = requests.get(teacher_url)
        soup = BeautifulSoup(res.content, "lxml")

        teacher_name = __get_teacher_name(soup)
        print("# target teacher: " + teacher_name)

        schedule_list = soup.find("div", class_="schedules-list")
        day_columns = schedule_list.find_all("ul", class_="oneday")

        # each day
        for day_column in day_columns:
            target_date = __get_schedule_date(day_column.find("li").get_text(), this_year)
            print("## target date: " + str(target_date))
            # each time
            for time_row in day_column.find_all("li", class_=lambda x: x != "date"):
                # Skip date row
                if not time_row.contents:
                    continue

                status = __get_status(time_row)
                print(status)


        sleep(3)
        # target_date = get_schedule_date(day_column.find("li").get_text(), this_year)
        #
        # print("id: " + id_)
        # print("name: " + teacher_name)
        # print(target_date)
        # print(day_columns)


def __get_target_ids():
    result = bookmark.get_teacher_ids()

    if not result:
        return []

    ids = []
    for id_tuple in result:
        ids.append(str(id_tuple[0]))

    return ids


def __get_teacher_name(soup):
    teacher_name = soup.find("h1")
    return teacher_name.get_text()


def __get_schedule_date(date_str, this_year):
    schedule_date = datetime.strptime(this_year + "-" + date_str[0:2] + "-" + date_str[3:5], "%Y-%m-%d")

    return schedule_date


def __get_status(time_row):
    status_text = time_row.get_text()

    if status_text == "終了":
        return Status.end
    elif status_text == "予約可":
        return Status.open
    elif status_text == "予約済":
        return Status.close

    


if __name__ == "__main__":
    scrape()
