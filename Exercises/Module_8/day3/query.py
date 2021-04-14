import sql_interface as sql 
import sqlite3
import pandas as pd 

#select = "SELECT name FROM student"
#print(len(sql.pandas_select(select)))

#select = "SELECT * FROM project WHERE namep = 'nlp'"
#print(sql.pandas_select(select))

#select = "SELECT * FROM teacher WHERE speciality='cv' AND salary > 2000"
#print(sql.pandas_select(select))

#column = "ALTER TABLE student ADD COLUMN favteacher char(40)"
#sql.sql_query(column)
#new = "SELECT * FROM student"
#print(sql.pandas_select(new))

#row = "DELETE FROM student WHERE name like 'M_%n'"
#sql.sql_query(row)
#new = "SELECT * FROM student"
#print(sql.pandas_select(new))

#select = "SELECT COUNT (DISTINCT name) name FROM student"
#print(len(sql.pandas_select(select)))

#select = "SELECT * FROM (project NATURAL JOIN (student))"
#print(sql.pandas_select(select))

#select = "SELECT max(project.grade) FROM project"
#print(sql.pandas_select(select))