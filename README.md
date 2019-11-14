#Log Analysis 
## what is this?

This is the frist project for the Udacity Full Stack Nanodegree. this a large data in SQL queries. The project is building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like,What are the most popular three articles of all time?,Who are the most popular article authors of all time?

 Udacity's Introduction to Programming Nanodegree.
### Installation
Requires Udacity’s Linux-based virtual machine and associated news-website database.

#### Requirements:
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


### Run Application
1. Clone the configuration from: https://github.com/udacity/fullstack-nanodegree-vm

2. Download [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

3. Type following command to your terminal to run this program:

* To lunch the virtual machine, type  ```vagrant up```, then login with command ```vagrant ssh```

* Use ```psql -d news -f newsdata.sql ``` to load data.

* Type ```python3 logs-analysis.py  ``` to run.

## Note:
The database includes three tables:
- Authors table
- Articles table
- Log table



