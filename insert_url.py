# encoding:utf-8
"""
将通过dmoz提取出的urls数据，导入到mysql数据库中
"""
from data_base import MySQL
import pandas as pd


def insert_db():

    url_set = pd.read_csv('csv/kt-content.csv')
    db = MySQL()
    for i in range(len(url_set)):
        print url_set.ix[i].values
        sql = 'Insert ignore into benign_urls(url,type)VALUES ("%s","%s")' % (url_set.ix[i].values[1],url_set.ix[i].values[2])
        db.insert_no_commit(sql)

    db.commit()
    db.close()

insert_db()