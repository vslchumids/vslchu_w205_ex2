############################################################################
# W205 Section 5 Exercise 2 Final Submission
# Vincent Chu
# File name  : finalresults.py
# Description: Seving script to return and print the total number of word 
#              occurrences in the Tweeter stream (stored in POSTGRES 
#              database). 
# Argument   : #1 string: Word for which number of occurrences will be 
#                         returned.  Total count of all words will be 
#                         returned if this argument was omitted. 
# Date       : 11/19/2016
############################################################################

from __future__ import absolute_import, print_function, unicode_literals
import sys
import psycopg2

def main(argv):
    try:
        # Connect to the tcount POSTGRES database
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
    except:
        print("Error: Cannot connect to the database tcount")
        exit()

    # If an argument was not given when the script was run
    if len(sys.argv) == 1:
        # Execute query to get all (word, count) pairs in ascending order of the words
        cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word")
        recs = cur.fetchall()
        recs_count = cur.rowcount

        index = 0
        results_str = ""

        # Iterate through the result set and build a string with each of the words
        # stored in the Tweetwordcount table of the tcount database and its count 
        # concatenated on a separate line
        for r in recs:
            index += 1
            results_str = results_str + "(<" + r[0] + ">, " + str(r[1]) + ")"
            if index < recs_count:
                results_str = results_str + ",\n"

        print(results_str)

    # If an argument was given as the lookup word when the script was run
    else:
        if len(sys.argv) > 2:
            print("Note: ", len(sys.argv), " arguments were given: only the first one will be used!\n", sep = "")

        try:
            # Execute query to get the number of occurrences for the word entered as argument
            cur.execute("SELECT count FROM Tweetwordcount WHERE word=%s", (sys.argv[1], ))
            word_count = cur.fetchone()[0]
            print("Total number of occurrences of \"", sys.argv[1], "\": ", word_count, sep = "")
        
        # Catch the no data found exception when the word entered is not in the 
        # Tweetwordcount table of the Tcount database, and print the number of 
        # occurrence as 0
        except:
            print("Total number of occurrences of \"", sys.argv[1], "\": 0", sep = "")

    conn.close()

if __name__ == '__main__':
    main(sys.argv)
