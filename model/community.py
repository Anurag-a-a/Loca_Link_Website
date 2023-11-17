import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)

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


def get_community_by_id(id):
    sql = "SELECT * FROM community WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql, (id,))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def get_communityName_by_id(id):
    sql = "SELECT name FROM community WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql, (id,))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def get_communityDescription_by_id(id):
    sql = "SELECT description FROM community WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql, (id,))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def get_community_id_by_communityName(name):
    sql = "SELECT id FROM community WHERE name='{}'".format(name)
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None

def get_communityList():
    sql = "SELECT id,name FROM community where userid = 1"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def addSubscription(userid,communityId):
    sql = "INSERT INTO subscription(communityId,userId) VALUES ('" + communityId + "','" + str(userid) + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def existSubscription(userid,commityId):
    sql = "SELECT count(1) FROM subscription where communityId='{}' and userId='{}'".format(commityId,userid)
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None