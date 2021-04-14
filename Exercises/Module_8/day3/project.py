import sql_interface as sql 
import sqlite3
import pandas as pd 

create_project_table = """CREATE TABLE project(
                            namep char(20) NOT NULL,
                            topic char(100) NOT NULL,
                            st int NOT NULL,
                            grade float(6),
                            id int NOT NULL PRIMARY KEY,
                            teacher char(20),
                            FOREIGN KEY(st,teacher) REFERENCES teacher(id,name)
                            );
                        """

#sql.sql_query(create_project_table)

sql.upload_data("project", "./project.csv")

select = "SELECT * FROM project"

print(sql.pandas_select(select))
