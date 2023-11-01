import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')

cur = conn.cursor()


def add_comment(content, postId, userId):
    sql = "INSERT INTO post(content,postId,userId) VALUES ('" + content + "','" + str(postId) + "','" + str(userId) + "')"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()


def get_comments_by_userId(userId):
    sql = "SELECT * FROM comment WHERE userId = '" + str(userId) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def get_comments_by_postId(postId):
    sql = "SELECT * FROM comment WHERE postId = '" + str(postId) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    if result:
        return result
    else:
        return []


def delete_comment(id):
    sql = "DELETE comment WHERE id = '" + str(id) + "'"
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    conn.cursor()
    conn.close()