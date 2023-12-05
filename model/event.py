import pymysql
from config import Config

config = Config()

conn = pymysql.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, db=config.DB_NAME,
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()


def add_event(userId, communityId, title, date, eventDesc, regURL, eventType, image_path):
    sql = "INSERT INTO event (userId, communityId, title, edate, eventDesc, regURL, eventType, imgURL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn.ping(reconnect=True)
    cur.execute(sql,(userId, communityId, title, date, eventDesc, regURL, eventType, image_path))
    conn.commit()
    conn.cursor()
    conn.close()


def exist_event(title):
    sql = "SELECT * FROM event WHERE title = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(title)))
    result = cur.fetchall()
    conn.commit()
    if (len(result) == 0):
        return False
    else:
        return True


def get_eventList_in_community(community_id):
    sql = "SELECT * FROM event WHERE communityId = %s "
    conn.ping(reconnect=True)
    cur.execute(sql,(str(community_id)))
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def get_event_by_id(event_id):
    sql = "SELECT * from event where id =  %s"
    conn.ping(reconnect=True)
    cur.execute(sql, str(event_id))
    result = cur.fetchone()
    conn.commit()
    if result:
        return result
    else:
        return None


def add_interestedNum(event_id):
    sql = "UPDATE event SET interestedNum = interestedNum + 1 WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(event_id)))
    conn.commit()
    conn.cursor()
    conn.close()


def delete_interestedNum(event_id):
    sql = "UPDATE event SET interestedNum = interestedNum - 1 WHERE id = %s"
    conn.ping(reconnect=True)
    cur.execute(sql,(str(event_id)))
    conn.commit()
    conn.cursor()
    conn.close()