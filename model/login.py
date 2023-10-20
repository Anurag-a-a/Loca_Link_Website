import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')
cur = conn.cursor()


def is_null(username, password):
    if (username == '' or password == ''):
        return True
    else:
        return False


def close(conn, cur):
    if cur:
        cur.close
    if conn:
        conn.close


def is_existed(username, password):
    sql = "SELECT * FROM user WHERE username ='" + username + "' and password ='" + password + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def exist_user(username):
    sql = "SELECT * FROM user WHERE username ='" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True