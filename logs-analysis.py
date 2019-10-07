
# logs-analysis  06-10-2019

import psycopg2

# 1). Finds the 3 most popular articles of all time
sql_query_articles = """
                    SELECT articles.title, CAST(count(log.path) AS text)
                    FROM articles
                    JOIN log ON
                        log.path like concat('%', articles.slug)
                    GROUP BY articles.title
                    ORDER BY count(log.path) desc
                    LIMIT 3;
                    """

# 2). Finds the 3 most popular authors.
sql_query_authors = """
                    SELECT authors.name, CAST(count(log.path) AS text)
                    FROM authors
                    JOIN articles ON
                        authors.id = articles.author
                    JOIN log ON
                        log.path like concat('%', articles.slug)
                    GROUP BY authors.name
                    ORDER BY count(log.path) DESC
                    LIMIT 3;
                    """

# 3). On what days did more that 1% of requests led to errors?
sql_query_errors = """
                   SELECT CAST(time::date AS text) as day,
                            CAST(ROUND(sum(case when status = '404 NOT FOUND'
                            then 1 else 0 end)*100.0/count(*), 2)
                            AS FLOAT)
                            AS errorpct
                    FROM log
                    GROUP BY day
                    HAVING sum(case when status = '404 NOT FOUND'
                               then 1 else 0 end)*100.0/count(*) > 1.0
                    """

query_list = [sql_query_articles, sql_query_authors, sql_query_errors]


# SQL Query Database section


def logs_connection(database_name):
    """Connects to the database
    Args: 
        database_name=the database connecting to (type-'string')
    """
    try:
        database = psycopg2.connect(dbname=database_name)
        return database
    except psycopg2.Error as e:
        print e


def logs_analysis(sql_query_list, database_name):
    """Queries the database, extracts the results and closes
    the database connection.
    Args:
        sql_query_list = a list of the SQL queries to be passed
                         to the database.
        database_name = the database connecting to. (string form)
    Returns:
            solutions_list = the results of each SQL query collated
                            into a single list.
    """
    db = logs_connection(database_name)
    cursor = db.cursor()
    try:
        solutions_list = []
        for query in sql_query_list:
            cursor.execute(query)
            solutions_list = solutions_list + [cursor.fetchall()]
        return solutions_list
    except psycopg2.Error as e:
        print e
    finally:
        cursor.close()
        db.close()


# Formatting Output Section


def format_authors_articles(unfmt_list):
    """Formats the authors' and articles' sections of the
    solutions_list returned from logs_analysis
    Args:
        unfmt_list = one of the elements of solutions_list
                    corresponding to SQL queries 1 & 2.
    Returns:
        the element from solutions_list formatted & ranked
    """
    ranking = 1
    for index in range(len(unfmt_list)):
        print(str(ranking) + '). '
              + str(unfmt_list[index][0])
              + ' --- ' + 'accessed '
                        + str(unfmt_list[index][1])
                        + ' times.'
              )
        ranking = ranking + 1


def format_errors(unfmt_list):
    """Formats the errors section of solutions_list
    returned from logs_analysis.
    Args:
        unfmt_list = the element(s) of solutions_list
                     corresponding to SQL query 3.
    """
    if unfmt_list != []:
        for index in range(len(unfmt_list)):
            print('On: '
                  + str(unfmt_list[index][0])
                  + ',   '
                  + str(unfmt_list[index][1])
                  + '% of requests led to errors'
                  )
    else:
        print 'No Days on which more than 1% of requests led to errors'


def final_solution_layout(solutions_list):
    """Formats all the elements from solutions_list returned from
    logs_analysis.
    Args:
        solutions_list = the results of each SQL query collated
                        into a single list (returned from
                        logs_analysis.)
    """
    for i in range(int(len(solutions_list)) - 1):
        print '\n'
        if i == 0:
            print ('What are the 3 most popular articles of all time? \n')
        else:
            print ('What are the 3 most popular authors of all time? \n')
        format_authors_articles(solutions_list[i])
    print ('\n' + 'On what days did more than 1% of request lead to errors?\n')
    format_errors(solutions_list[int(len(solutions_list)) - 1])


final_solution_layout(logs_analysis(query_list, "news"))
