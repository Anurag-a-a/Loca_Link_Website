import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')
cur = conn.cursor()


def add_community(name, userId):
    sql = "INSERT INTO community(name,userId) VALUES ('" + name + "','" + userId + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def exist_community(name):
    sql = "SELECT * FROM user WHERE name ='" + name + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True