import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', db='team20')
cur = conn.cursor()


def add_user(username, password):
    # sql commands
    sql = "INSERT INTO students(name, password) VALUES ('" + username + "','" + password + "')"
    conn.ping(reconnect=True)
    # execute(sql)
    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.cursor()
    conn.close()