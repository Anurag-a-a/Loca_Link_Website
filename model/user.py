import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')
cur = conn.cursor()


def is_null(username, password):
    if (username == '' or password == ''):
        return True
    else:
        return False
    

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


def add_user(username, password, email):
    sql = "INSERT INTO user(username, password, email) VALUES ('" + username + "','" + password + "','" + email + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()


def get_user_id_by_username(username):
    sql = "SELECT id FROM user WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result[0]
    else:
        return None


def close(conn, cur):
    if cur:
        cur.close
    if conn:
        conn.close