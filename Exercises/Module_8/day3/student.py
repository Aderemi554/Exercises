import sql_interface as sql 
import sqlite3
import pandas as pd 

create_student_table = """CREATE TABLE student(
                            name char(20) NOT NULL,
                            surname char(20) NOT NULL,
                            id int NOT NULL PRIMARY KEY,
                            country char(20),
                            FOREIGN KEY(id) REFERENCES project(st)
                            );
                        """

sql.upload_data("student", "./student.csv")

select = "SELECT * FROM student"

print(sql.pandas_select(select))
