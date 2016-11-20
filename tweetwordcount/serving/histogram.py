############################################################################
# W205 Section 5 Exercise 2 Final Submission
# Vincent Chu
# File name  : histogram.py
# Description: Seving script to display the words with counts between the 
#              2 numbers given as arguments.  If only 1 number was given,  
#              it would be treated as the lower bound.  Error messages will
#              be displayed if the inputs are not numeric or if the lower
#              bound number > the upper bound number.
# Argument   : #1 number: lower bound of the range of word occurrences
#              #2 number: upper bound of the range of word occurrences
#              
# Date       : 11/19/2016
############################################################################

from __future__ import absolute_import, print_function, unicode_literals
import sys
import psycopg2

def main(argv):
    try:
        # Connect to the POSTGRES database named tcount
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
    except:
        print("Error connecting to the database tcount")
        exit()

    # If an argument was not given when the script was run
    if len(sys.argv) == 1:
        print("Error: You must provide the range for the number of word occurrences!")

    # If only 1 argument was given when the script was run, then the all the words with 
    # occurrences more than the argument will return 
    elif len(sys.argv) == 2: 

        try:
            # convert the input argument from string to float and round it to integer 
            l_limit = int(round(float(sys.argv[1])))
        except:
            print("Error: Your input as the lower bound for the number of word occurrences must be a number")
            exit()

        try:
            # Execute query to get words (and corresponding counts) with number of 
            # occurrences >= the argument 
            cur.execute("SELECT word, count FROM Tweetwordcount WHERE count >= %s ORDER BY count DESC", (str(l_limit), ))
            recs = cur.fetchall()

            results_str = ""
            index = 0
            recs_count = cur.rowcount

            # Iterate through the result set and build a string with all the words
            # whose count is more than or equal to the argument given
            for r in recs:
                index += 1
                results_str = results_str + "<" + r[0] + ">: " + str(r[1])

                # Add a line break for all items in the result except the very last
                if index < recs_count:
                    results_str = results_str + "\n"

            # Output message if the query didn't return any results where the count
            # is >= the lower bound argument
            if results_str == "":
                print("Note: No words have occurrences >=", l_limit)
            else:    
                print(results_str)


        # Catch the no data found exception when no records were found with count >=
        # the argument given
        except:
            print("Note: No words have occurrences >=", l_limit)

    # If at least 2 arguments were given when the script was run as the range of 
    # number of occurrences to look for
    else:

        try:
            # convert the input arguments from string to float and round it to integer 
            l_limit = int(round(float(sys.argv[1])))
            u_limit = int(round(float(sys.argv[2])))
        except:
            print("Error: Your inputs as the range for the number of word occurrences must be numbers")
            exit()

        # Output error meassge and exit script if the upper bound number < the lower 
        # bound number    
        if u_limit < l_limit:
            print("Error: The lower bound must be <= the upper bound in your inputs")
            exit()

        try:
            # Execute query to get words (and corresponding counts) with number of 
            # occurrences between the arguments 
            cur.execute("SELECT word, count FROM Tweetwordcount WHERE count >= %s AND count <= %s ORDER BY COUNT DESC", (l_limit, u_limit))
            recs = cur.fetchall()

            results_str = ""
            index = 0
            recs_count = cur.rowcount

            # Iterate through the result set and build a string with all the words
            # whose count is between the arguments given
            for r in recs:
                index += 1
                results_str = results_str + "<" + r[0] + ">: " + str(r[1])
                
                # Add a line break for all items in the result except the very last
                if index < recs_count:
                    results_str = results_str + "\n"

            # Output message if the query didn't return any results where the count
            # is between the arguments
            if results_str == "":
                print("Note: No words have occurrences >=", l_limit, "and <=", u_limit)
            else:
                print(results_str)

        # Catch the no data found exception when no records were found with count
        # between the arguments given
        except:
            print("Note: No words have occurrences >=", l_limit, "and <=", u_limit)
 

if __name__ == '__main__':
    main(sys.argv)
