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
    

def is_existed(username):
    sql = "SELECT id, username, password,location FROM user WHERE username =%s"
    conn.ping(reconnect=True)
    cur.execute(sql,(username))
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return result[0]


def exist_user(username):
    sql = "SELECT * FROM user WHERE username =%s "
    conn.ping(reconnect=True)
    cur.execute(sql,(username))
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def add_user(username, password, email,location):
    sql = "INSERT INTO user( username, password, email, location) VALUES (%s,%s,%s,%s)"
    conn.ping(reconnect=True)
    cur.execute(sql,(username,password, email,location))
    conn.commit()


def get_user_id_by_username(username):
    sql = "SELECT id FROM user WHERE username = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(username ))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None

def get_profile(username):
    sql = "SELECT * FROM user WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def change_user_password(username, new_password):
    sql = "UPDATE user SET password = '" + new_password + "' WHERE username = '" + username + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()

def updatePass(username,password):
    sql = "UPDATE user SET  password = %s WHERE username = %s"
    values = (password,username)
    conn.ping(reconnect=True)
    cur.execute(sql,values)
    conn.commit()

def updateDetails(username,email,description,address,phone,avatar):
    sql = "UPDATE user SET  email = %s,description = %s, address = %s, phone = %s, avatar = %s WHERE username = %s"
    values = (email,str(description), str(address), str(phone), avatar, username)
    conn.ping(reconnect=True)
    cur.execute(sql,values)
    conn.commit()

def close(conn, cur):
    if cur:
        cur.close
    if conn:
        conn.close