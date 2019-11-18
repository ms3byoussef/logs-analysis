import psycopg2

#connect to the database
dbname="news"


conn= psycopg2.connect(database=dbname)

#the cursor

c = conn.cursor()

#the query title

query_title1 ="the most popular three articles of all time:"

#query of the most popular articles

query1="""select articles.title, count(*) as Views 
from articles,log 
where log.path = concat('/article/', articles.slug)
group by articles.title 
order by Views  desc limit 3;"""

#the cursor execute 

c.execute(query1)

#the results

myresults1=c.fetchall()

#print the query

print("The QUERY 1"+"\n"+query_title1 + "\n")

for result in myresults1:
        print('\t' + str(result[0]) + " - " + str(result[1]) + " Views  " + "\n")



#the secand query 

#the query title
query_title2 ="the most popular article authors of all time:"

#query of the most popular article authors

query2=""" SELECT authors.name, COUNT(*) As Views 
    FROM authors
    INNER JOIN articles
      ON authors.id = articles.author
    INNER JOIN log
      ON log.path LIKE concat('/article/', articles.slug)
    GROUP BY authors.name
    ORDER BY Views  desc;
    """

#the cursor execute 

c.execute(query2)

#the results

myresults2=c.fetchall()

#print the query

print("The QUERY 2"+"\n"+query_title2 + "\n")

for result in myresults2:
       print('\t' + str(result[0]) + " - " + str(result[1]) + " views "+ "\n")


#the third query 

#the query title
query_title3 ="On which days did more than 1% of requests lead to errors"

#query of On which days did more than 1% of requests lead to errors

query3=""" SELECT *
            FROM (select date(time), ROUND (100.0 * sum (CASE log.status
            WHEN '200 OK' THEN 0 else 1 end)
            /COUNT (log.status), 3) AS error 
            FROM log
            GROUP BY date(time)
            ORDER BY error desc) AS subq WHERE error > 1;
"""

#the cursor execute 

c.execute(query3 )

#the results

myresults3=c.fetchall()

#print the query 3

print("The QUERY 3"+"\n"+query_title3 + "\n")

for result in myresults3:
        print('\t' + str(result[0]) + " - " + str(result[1]) + " % "+"\n")
conn.close()
