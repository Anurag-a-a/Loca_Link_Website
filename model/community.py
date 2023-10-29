import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')
cur = conn.cursor()


def add_community(name, userId):
    sql = "INSERT INTO community(name,userId) VALUES ('" + name + "','" + str(userId) + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def exist_community(name):
    sql = "SELECT * FROM community WHERE name ='" + name + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def get_community_id_by_communityName(name):
    sql = "SELECT id FROM community WHERE name = '" + name + "'"
    conn.ping(reconnect=True)
    cur.execute(sql, (name,))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result[0]
    else:
        return None