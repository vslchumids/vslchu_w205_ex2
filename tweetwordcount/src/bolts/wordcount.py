############################################################################
# W205 Section 5 Exercise 2 Final Submission
# Vincent Chu
# File name  : wordcount.py
# Description: Script to serve as the bolt that counts the number of words
#              emitted by the spout of the Streamparse project and stores/ 
#              updates the count in the Tweetwordcount table of the 
#              POSTGRES database t_count.
# Date       : 11/18/2016
############################################################################

from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.

        cur.execute("SELECT COUNT(*) FROM Tweetwordcount WHERE word=%s", (word, ))
        word_count = cur.fetchone()[0]

        #self.log("word count = %s", word_count)

        if word_count > 0:
            cur.execute("UPDATE Tweetwordcount SET count=count+1 WHERE word=%s", (word, ))
            self.log('After UPDATE: word count = %d' % (word_count))
        else:
            cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES (%s, 1)", (word, ))
            self.log('After INSERT: word count = %d' %  (word_count))

        conn.commit()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        #self.log('%s: %d' % (word, self.counts[word]))
