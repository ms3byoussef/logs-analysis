#! /usr/bin/env python3

import psycopg2
DBNAME = "news"

def connect(DBNAME="news"):
    """Connect to the  database."""
    db = psycopg2.connect('dbname=' + DBNAME)
    cursor = db.cursor()
   
    return db, cursor

def get_results(query):
    """Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()
    
result=get_results(query)
# What are the most popular three articles of all time?

title_1 = ("What are the most popular three articles of all time?")
query_1 = """
        SELECT articles.title, COUNT(*) AS views
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP ByY articles.title
        ORDER BY views DESC
        LIMIT 3;
   """

 
# Who are the most popular article authors of all time?
title_2 = ("Who are the most popular article authors of all time?")
query_2 = """"
SELECT authors.name,COUNT(article_view.views) AS views
FROM article_view,authors
where authors.id = article_view.author
GROUP By authors.name
ORDER BY views desc"""

def print("\n2. Who are the most popular article authors of all time?")
 cursor.execute(query_2)
   result= cursor.fetchall()
for i in result:
    
# On which days did more than 1% of requests lead to errors
title_3 = ("On which days did more than 1% of requests lead to errors?")
query_3 = """
SELECT total.day,
          ROUND(((errors.eerror_results*1.0) / total.results), 3) AS perc
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_results
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS results
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_results*1.0) / total.results), 3) > 0.01)
        ORDER BY perc DESC;
 """

 def print_query_1(query_result):
    
print("\n1. What are the most popular three articles of all time?")
num=1
for i in result: 
      print('(' + str(num) + ')' + i [0] + " with ' + str(i[1]) + " views")
        num += 1

def print_query_2(query_result):
    
print("\n2. Who are the most popular article authors of all time?")
num=1
for i in result: 
      print('(' + str(num) + ')' + i [0] + " with ' + str(i[1]) + " views")
        num += 1





def print_error(query-error):
    print (" \n3.On which days did more than 1% of requests lead to errors?")
    for result in  :
        print ('\t' + str(result[0]) + '  ' + str(result[1]) + ' %')
 # the query result
articles_results = get_result(query_1)
authors_results = get_result(query_2)
error_days_results= get_result(query_3)

# print the output
print_query_1(articles_results)
print_query_2(authors_results)
print_error(error_days_results)
