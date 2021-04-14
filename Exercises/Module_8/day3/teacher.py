import sql_interface as sql 
import sqlite3
import pandas as pd 

create_teacher_table = """CREATE TABLE teacher(
                            name char(20) NOT NULL,
                            surname char(20) NOT NULL,
                            id int NOT NULL PRIMARY KEY,
                            country char(20),
                            specialty char(50),
                            salary int(10),
                            FOREIGN KEY(id) REFERENCES project(st)
                            );
                        """

#sql.sql_query(create_teacher_table)

sql.upload_data("teacher", "./teacher.csv")

select = "SELECT * FROM teacher"

print(sql.pandas_select(select))