import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()


def is_null_login(username, password):
    if (username == '' or password == ''):
        return True
    else:
        return False


def is_null_signup(username, password, email):
    if (username == '' or password == '' or email == ''):
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
        return result
    else:
        return None


def get_password_by_username(username):
    sql = "SELECT password FROM user WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result["password"]
    else:
        return None


def get_email_by_username(username):
    sql = "SELECT email FROM user WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result["email"]
    else:
        return None


def change_user_password(username, new_password):
    sql = "UPDATE user SET password = '" + new_password + "' WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()


def change_email(username, new_email):
    sql = "UPDATE user SET email = '" + new_email + "' WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()


def close(conn, cur):
    if cur:
        cur.close
    if conn:
        conn.close