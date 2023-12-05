import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

def add_like(userId,postId):
    sql = "INSERT INTO likestate (userId, postId) VALUES (%s, %s)"
    conn.ping(reconnect=True)
    cur.execute(sql, (str(userId), str(postId)))
    conn.commit()


def if_liked(userId, postId):
    sql = "SELECT * FROM likestate WHERE userId = %s and postId = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(userId),str(postId)))
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def get_like(userId, postId):
    sql = "SELECT id FROM likestate WHERE userId = %s and postId = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(userId),str(postId) ))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def delete_like(id):
    sql = "DELETE FROM likestate WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql, (str(id)))
    conn.commit()
    conn.close()