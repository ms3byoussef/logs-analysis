#Log Analysis 
## what is this?

This is the frist project for the Udacity Full Stack Nanodegree. this a large data in SQL queries. The project is building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like,What are the most popular three articles of all time?,Who are the most popular article authors of all time?

 Udacity's Introduction to Programming Nanodegree.
### Installation
Requires Udacity’s Linux-based virtual machine and associated news-website database.
Instructions for installing the VM and data follow.
#### Requirements:
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

#### Installing the dependencies and setting up the files:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
1. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data to get the newsdata.sql file.
1. Put the newsdata.sql file into the vagrant directory
1. Upzip as needed and copy all files into the vagrant directory into a folder called log_analysis
#### Start the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/log_analysis ```
### Run Application
Log in to VM.
```
vagrant ssh
```
cd into shared directory:
```
$ cd /vagrant
```
Commandline should now look like this:
``` vagrant@vagrant:/vagrant$ ```

Run:
```
$ python logs-analysis-rev.py
```
## Note:
The database includes three tables:
- Authors table
- Articles table
- Log table



