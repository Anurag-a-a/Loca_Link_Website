import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')
cur = conn.cursor()


def add_post(userId, communityId, title, content):
    sql = "INSERT INTO community(name,userId,title,content) VALUES ('" + userId + "','" + communityId + "','" + title + "','" + content + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def exist_post(title):
    sql = "SELECT * FROM post WHERE title ='" + title + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True