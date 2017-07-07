import os
import psycopg2
import urllib.parse


def get_teacher_ids():
    conn = __get_conn()
    cur = conn.cursor()

    cur.execute("select distinct teacher_id from bookmark")

    result = cur.fetchall()

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
