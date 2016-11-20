############################################################################
# W205 Section 5 Exercise 2 Final Submission
# Vincent Chu
# File name  : README.txt
# Description: Instructions for running the project
# Date       : 11/19/2016
############################################################################

############################################################################
# Start-up and Installation
############################################################################
$ /data/start_postgres.sh
$ su - w205 
$ pip install tweepy
$ pip install psycopg2

############################################################################
# Steps to run my Exercise 2 Streamparse Project using git clone
############################################################################
$ cd /home/w205/
$ git clone https://github.com/vslchumids/vslchu_w205_ex2.git
$ cd vslchu_w205_ex2
$ bash run_ex2.sh

############################################################################
# Steps to run my Exercise 2 Streamparse Project by downloading zip file
############################################################################
$ cd /home/w205/
$ wget https://github.com/vslchumids/vslchu_w205_ex2/archive/master.zip
$ unzip master.zip
$ mv vslchu_w205_ex2-master vslchu_w205_ex2
$ cd vslchu_w205_ex2
$ bash run_ex2.sh
