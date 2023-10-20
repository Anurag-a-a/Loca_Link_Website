import pymysql

conn = pymysql.connect(host='localhost', user='root', password='rootroot', db='team20')
cur = conn.cursor()
email = 'amsdasd@gmail.com'
adm = '0'


def add_user(username, password):
    # sql commands
    sql = "INSERT INTO user(username, password,email,isAdm) VALUES ('" + username + "','" + password + "','" + email + "','" + adm + "' )"
    conn.ping(reconnect=True)
    # execute(sql)
    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.cursor()
    conn.close()