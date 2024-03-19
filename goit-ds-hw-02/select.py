from psycopg2 import Error
import psycopg2
from connect import connection_parameters


def select_projects(con):
    """
    Query all rows in the tasks table
    :param con: the Connection object
    :return: rows projects
    """
    rows = None
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_all_tasks(con):
    """
    Query all rows in the tasks table
    :param con: the Connection object
    :return: rows tasks
    """
    rows = None
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_task_by_status(con, status):
    """
    Query tasks by priority
    :param con: the Connection object
    :param status:
    :return: rows tasks
    """
    rows = None
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = 'new')")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


if __name__ == '__main__':
    with psycopg2.connect(**connection_parameters) as conn:
        print("Users:")
        projects = select_projects(conn)
        print(projects)
        print("Tasks")
        tasks = select_all_tasks(conn)
        print(tasks)
        print("Tasks by status:")
        task_by_priority = select_task_by_status(conn, 'new')
        print(task_by_priority)
