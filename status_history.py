import os
import psycopg2
import urllib.parse
from datetime import datetime


def save_history(teacher_id, name, status, class_date):
    conn = __get_conn()
    cur = conn.cursor()

    cur.execute("insert into status_history(teacher_id, name, status, class_date, acquisition_date) "
                "values(%s, %s, %s, %s, %s)", (teacher_id, name, status, class_date, datetime.now()))

    conn.commit()

    cur.close()
    conn.close()


def get_history(teacher_id, status, class_date):
    conn = __get_conn()
    cur = conn.cursor()

    cur.execute("select teacher_id,name,status,class_date from status_history "
                "where teacher_id = %s and status = %s and class_date = %s",
                (teacher_id, status, class_date))

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result


def __get_conn():
    urllib.parse.uses_netloc.append("postgres")
    url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    return conn
