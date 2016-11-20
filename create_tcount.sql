----------------------------------------------------------------------------
-- W205 Section 5 Exercise 2 Final Submission
-- Vincent Chu
-- File name: create_tcount.sql
-- Description: SQL script to create the tcount database and the 
--              Tweetwordcount table in POSTGRES
-- Date       : 11/17/2016
----------------------------------------------------------------------------

CREATE DATABASE tcount;

\c tcount;

DROP TABLE Tweetwordcount;

CREATE TABLE Tweetwordcount
(
    word text,
    count integer
);

SELECT * FROM Tweetwordcount ORDER BY count DESC LIMIT 20;