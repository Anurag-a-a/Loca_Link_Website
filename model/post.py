import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()


def add_post(userId, communityId, title, content, image_path):
    sql = "INSERT INTO post (userId, communityId, title, content, imgURL) VALUES (%s, %s, %s, %s, %s)"
    conn.ping(reconnect=True)
    cur.execute(sql,(userId, communityId, title, content, image_path))
    conn.commit()
    conn.cursor()
    conn.close()

def add_event(userId, communityId, title, date, eventDesc, regURL, eventType, image_path):
    sql = "INSERT INTO event (userId, communityId, title, edate, eventDesc, regURL, eventType, imgURL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn.ping(reconnect=True)
    cur.execute(sql,(userId, communityId, title, date, eventDesc, regURL, eventType, image_path))
    conn.commit()
    conn.cursor()
    conn.close()


def exist_post(title):
    sql = "SELECT * FROM post WHERE title = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(title))
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True

def exist_event(title):
    sql = "SELECT * FROM event WHERE title = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(title))
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def get_postList_in_community(community_id):
    sql = "SELECT * FROM post WHERE isdeleted=0 and communityId = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,str(community_id))
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def get_eventList_in_community(community_id):
    sql = "SELECT * FROM event WHERE communityId = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(community_id))
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def get_post_by_id(post_id):
    sql = "SELECT * from post where id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(post_id)))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None

   
def add_likeNum(post_id):
    sql = "UPDATE post SET likeNum=likeNum+1 WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(post_id)))
    conn.commit()
    conn.cursor()
    conn.close()


def delete_likeNum(post_id):
    sql = "UPDATE post SET likeNum=likeNum-1 WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(post_id)))
    conn.commit()
    conn.cursor()
    conn.close()

def get_usersPosts(id):
    sql = "SELECT id, title, content,imgURL, createTime FROM post where userid = %s and isDeleted = 0"
    conn.ping(reconnect=True)
    cur.execute(sql, (id,))
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []

def get_usersEvents(id):
    sql = "SELECT * FROM event where userid = %s"
    conn.ping(reconnect=True)
    cur.execute(sql, (id,))
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def delete_post_by_id(id):
   
    sql = "UPDATE post SET isDeleted = 1 WHERE id = %s"
    try:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        rows_affected = cur.rowcount
        if rows_affected == 1:
            return True
        else:
            return False
    except Exception as e:
        return False
