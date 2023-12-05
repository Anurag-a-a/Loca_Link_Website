import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

def add_interested(userId,eventId):
    sql = "INSERT INTO interested (userId, eventId) VALUES (%s, %s)"
    conn.ping(reconnect=True)
    cur.execute(sql, (str(userId), str(eventId)))
    conn.commit()


def if_interested(userId, eventId):
    sql = "SELECT * FROM interested WHERE userId ='" + str(userId) + "' and eventId ='" + str(eventId) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def get_interested(userId, eventId):
    sql = "SELECT id FROM interested WHERE userId = '" + str(userId) + "' and eventId = '" + str(eventId) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def delete_interested(id):
    sql = "DELETE FROM interested WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql, (str(id)))
    conn.commit()
    conn.close()