# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import mysql.connector

class GoogleProjectPipeline(object):
    def process_item(self, item, spider):
       # self.create_connection()
        #self.create_table()
        return item

    '''def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1q2w3e4r5t',
            database='googleclouddatastore'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXITS extract_tb""")
        self.curr.execute("""CREATE TABLE extract_tb(
                    title text
                    links text
                    )
                    """)
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into extract_tb values (%s,%s)""", (
            item['title'][0],
            item['links'][0]
        ))
        self.conn.commit() '''