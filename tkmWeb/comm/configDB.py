import  logging
import pymysql
from config import  config
def get_db_conn():
    conn=pymysql.connect(host=config.host,port=config.port,
                         user=config.user,passwd=config.password,db=config.database)
    return conn

def query_db(sql):
    conn=get_db_conn()
    cursor=conn.cursor()
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
    except Exception as  e:
        print(e)
    cursor.close()
    conn.close()
    return  data
def util_db(sql):
    conn=get_db_conn()
    cursor=conn.cursor()
    try:
        cursor.execute(sql)
        logging.info(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error( (e.massege))
    cursor.close()
    conn.close()


if __name__ == '__main__':
    sql='SELECT * from  smslog WHERE telNos="18604760926"'
    print(query_db(sql))