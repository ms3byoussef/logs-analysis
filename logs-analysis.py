#! /usr/bin/env python3

import psycopg2
DB_NAME = "news"


db = psycopg2.connect(database=DB_NAME)
cursor = db.cursor() 


# What are the most popular three articles of all time?
query_1_title = ("What are the most popular three articles of all time?")
query_1 = "select articles.title , count(log.path) as views from articles" \
    " left join log on log.path like '%' || articles.slug where log.status " \
    "= '200 OK' group by articles.title order by views desc limit 3"

# Who are the most popular article authors of all time?
query_2_title = ("Who are the most popular article authors of all time?")
query_2 = "select authors.name , t1.views from authors, (select articles.author" \
    " as author , count(log.path) as views from articles left join log on" \
    " log.path like '%' || articles.slug where log.status = '200 OK' group " \
    "by articles.author order by views desc) as t1 where t1.author = " \
    "authors.id"

# On which days did more than 1% of requests lead to errors
query_3_title = ("On which days did more than 1% of requests lead to errors?")
query_3 = "select t1.date, round((t2.errors::NUMERIC / t1.total) * 100 ,1) as " \
    "result from (select date_trunc('day', time) as date, count(1) as" \
    " total from log group by 1) as t1, (select date_trunc('day', time)" \
    " as date, count(1) as errors from log where log.status != '200 OK'" \
    " group by 1) as t2 where t1.date = t2.date and " \
    "round((t2.errors::NUMERIC / t1.total) * 100 ,1) > 1"


print("\n1. What are the most popular three articles of all time?")
Cursor.execute(query_1)
for table in Cursor.fetchall():
    print("  - \"{}\" - {} views".format(table[0], table[1]))


print("\n2. Who are the most popular article authors of all time?")
cursor.execute(query_2)
for table in cursor.fetchall():
    print("  - {} - {} views".format(table[0], table[1]))


print("\n3. On which days did more than 1% of requests lead to errors?")
cursor.execute(query_3)
for table in cursor.fetchall():
    date = table[0].strftime('%b %d,%Y')
    print("  - {} - {}% errors".format(date, table[1]))

db.close()
