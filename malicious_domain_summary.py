import time
import MySQLdb


def mysql_handle(table,time_limit_left,time_limit_right):
    timeArray_limit_left = time.strptime(time_limit_left, "%Y-%m-%d %H:%M:%S")
    timeStamp_limit_left = int(time.mktime(timeArray_limit_left))
    timeArray_limit_right = time.strptime(time_limit_right, "%Y-%m-%d %H:%M:%S")
    timeStamp_limit_right = int(time.mktime(timeArray_limit_right))
    db = MySQLdb.connect(
        "172.29.152.249 ", "root", "platform", "malicious_domain_collection")
    cursor = db.cursor()
    sql = "select domain,insert_time from " + table
    cursor.execute(sql)
    results = cursor.fetchall()
    flag_commit = 0
    countsus = 0
    for row in results:
        insert_time = str(row[1])
        domain = row[0]
        timeArray = time.strptime(insert_time, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        if timeStamp < timeStamp_limit_right and timeStamp > timeStamp_limit_left:
                value = [domain,insert_time]
                sql = "insert ignore into malicious_domain_collection_new (domain,insert_time) values(%s,%s)"
                cursor.execute(sql, value)
                rowsaffected = cursor.rowcount
                if (rowsaffected == 1):
                    countsus = countsus + 1
                flag_commit = flag_commit + 1
                if flag_commit == 1000:
                    print 1000
                    db.commit()
                    flag_commit = 0
        else:
            continue
    db.commit()
    print countsus
    db.close()


def hosts_domain():
    mysql_handle("hosts_domains","2018-01-08 20:00:00","2018-01-15 20:00:00")