import psycopg2
from connect import connection_parameters


def create_table(con, create_table_sql):
    """ create a table from the create_table_sql statement
    :param con: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    with con.cursor() as cur:
        # Створення нової таблиці
        cur.execute(create_table_sql)
        print("Table created successfully")
        con.commit()  # Збереження змін у базі даних


if __name__ == '__main__':
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id integer PRIMARY KEY AUTOINCREMENT,
     fullname VARCHAR(100),
     email VARCHAR(100),
     CONSTRAINT email_un UNIQUE (email)
     );
    """

    sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
     id integer PRIMARY KEY,
     name VARCHAR(50),
     CONSTRAINT name_un UNIQUE (name)
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id integer PRIMARY KEY AUTOINCREMENT,
     title VARCHAR(100),
     description text,
     status_id INT,
     user_id INT,
     FOREIGN KEY (status_id) REFERENCES status (id),
     FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
    );
    """

    with psycopg2.connect(**connection_parameters) as conn:
        if conn is not None:
            # create users table
            create_table(conn, sql_create_users_table)
            # create status table
            create_table(conn, sql_create_status_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")
