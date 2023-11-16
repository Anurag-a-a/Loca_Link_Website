import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()


def add_post(userId, communityId, title, content):
    sql = "INSERT INTO post(userId,communityId,title,content) VALUES ('" + str(userId) + "','" + str(communityId) + "','" + title + "','" + content + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def exist_post(title):
    sql = "SELECT * FROM post WHERE title ='" + title + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def get_postList_in_community(community_id):
    sql = "SELECT * FROM post WHERE communityId = '" + str(community_id) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def add_like(user_id, post_id):
    sql = "INSERT INTO likestate(userId,postId) VALUES ('" + str(user_id) + "','" + str(post_id) + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()

def get_post_by_id(post_id):
    sql = "SELECT * from post where id = '" + str(post_id) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None

    
def add_likeNum(post_id):
    sql = "UPDATE post SET likeNum=likeNum+1 WHERE id = '" + str(post_id) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def delete_like(user_id, post_id):
    sql = "DELETE likestate WHERE userId = '" + str(user_id) + "' AND postId = '" + str(post_id) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def delete_likeNum(post_id):
    sql = "UPDATE post SET likeNum=likeNum-1 WHERE id = '" + str(post_id) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()
