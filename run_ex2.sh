############################################################################
# W205 Section 5 Exercise 2 Final Submission
# Vincent Chu
# File name  : run_ex2.sh
# Description: sh script to 
# Date       : 11/19/2016
############################################################################

mkdir /home/w205/exercise_2/
cd /home/w205/exercise_2/

sparse quickstart tweetwordcount
cd tweetwordcount
rm topologies/wordcount.clj
rm src/spouts/words.py
rm src/bolts/wordcount.py

cp /home/w205/vslchu_w205_ex2/tweetwordcount/topologies/tweetwordcount.clj /home/w205/exercise_2/tweetwordcount/topologies/.
cp /home/w205/vslchu_w205_ex2/tweetwordcount/src/spouts/tweets.py /home/w205/exercise_2/tweetwordcount/src/spouts/.
cp /home/w205/vslchu_w205_ex2/tweetwordcount/src/bolts/parse.py /home/w205/exercise_2/tweetwordcount/src/bolts/.
cp /home/w205/vslchu_w205_ex2/tweetwordcount/src/bolts/wordcount.py /home/w205/exercise_2/tweetwordcount/src/bolts/.
cp /home/w205/vslchu_w205_ex2/tweetwordcount/serving/finalresults.py /home/w205/exercise_2/.
cp /home/w205/vslchu_w205_ex2/tweetwordcount/serving/histogram.py /home/w205/exercise_2/.
cp /home/w205/vslchu_w205_ex2/create_tcount.sql /home/w205/exercise_2/.

cd /home/w205/exercise_2/
psql -U postgres -f create_tcount.sql

cd /home/w205/exercise_2/tweetwordcount/
sparse run