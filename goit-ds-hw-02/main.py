import psycopg2
from psycopg2 import Error
from connect import connection_parameters
from create_table import create_table


sql_create_users_table = """
CREATE TABLE IF NOT EXISTS users (
 id SERIAL PRIMARY KEY,
 fullname VARCHAR(100),
 email VARCHAR(100),
 CONSTRAINT email_un UNIQUE (email)
 );
"""

sql_create_status_table = """
CREATE TABLE IF NOT EXISTS status (
 id INT PRIMARY KEY,
 name VARCHAR(50),
 CONSTRAINT name_un UNIQUE (name)
);
"""

sql_status_table_fill = """
INSERT INTO status (id, name)
VALUES (1, 'new'), (2, 'in progress'), (3, 'completed');
"""

sql_create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
 id SERIAL PRIMARY KEY,
 title VARCHAR(100),
 description text,
 status_id INT,
 user_id INT,
 FOREIGN KEY (status_id) REFERENCES status (id),
 FOREIGN KEY (user_id) REFERENCES users (id)
    ON DELETE CASCADE
);
"""

sql_clean_table = "TRUNCATE TABLE status;"


def sql_request(con, request):
    cur = con.cursor()
    try:
        cur.execute(request)
        con.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    with psycopg2.connect(**connection_parameters) as conn:
        if conn is not None:
            # видалення таблиць:
            sql_request(conn, "DROP TABLE tasks;")
            sql_request(conn, "DROP TABLE users;")
            sql_request(conn, "DROP TABLE status;")
            # створення таблиці users
            create_table(conn, sql_create_users_table)
            # створення таблиці status
            create_table(conn, sql_create_status_table)
            # створення таблиці tasks
            create_table(conn, sql_create_tasks_table)

        else:
            print("Error! cannot create the database connection.")
