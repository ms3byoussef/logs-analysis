#! /usr/bin/env python3

import psycopg2
DB_NAME = "news"

  
def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results  


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

def print_query_results(query_results):
    print (query_results[1])
    for index, results (query_results[0]):
        print (
            "\t", index+1, "-", results[0],
            "\t - ", str(results[1]), "views")


def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ("\t", results[0], "-", str(results[1]) + "% errors")


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(query_1), query_1_title
    popular_authors_results = get_query_results(query_2), query_2_title
    load_error_days = get_query_results(query_3), query_3_title

    # print query results
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
