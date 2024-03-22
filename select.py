from psycopg2 import Error
import psycopg2
from connect import connection_parameters


def sql_request(con, req):
    rows = None
    cur = con.cursor()
    try:
        cur.execute(req)
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def sql_update(con, req):
    cur = con.cursor()
    try:
        cur.execute(req)
    except Error as e:
        print(e)
    finally:
        con.commit()
        cur.close()


if __name__ == '__main__':
    with psycopg2.connect(**connection_parameters) as conn:
        # Отримати всі завдання певного користувача.
        print("Tasks by user")
        name = input("Enter full user name: ")
        request = f"SELECT * FROM tasks WHERE user_id IN (SELECT id FROM users WHERE fullname = '{name}')"
        print(sql_request(conn, request))

        # Вибрати завдання за певним статусом.
        print("Tasks by status")
        status = input("Enter status: ")
        request = f"SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = '{status}')"
        print(sql_request(conn, request))

        # Оновити статус конкретного завдання.
        print("Change task status")
        task = input("Enter task title: ")
        status = input("Enter task status: ")
        request = f"""UPDATE tasks SET status_id =
                  (SELECT id FROM status WHERE name = '{status}')
                  WHERE title = '{task}';"""
        sql_update(conn, request)
        print("Task status updated")

        # Отримати список користувачів, які не мають жодного завдання.
        print("Users free of tasks")
        request = "SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)"
        print(sql_request(conn, request))

        # Додати нове завдання для конкретного користувача.
        print("Adding new task")
        task = input("Enter task title: ")
        name = input("Enter full user name: ")
        request = f"""INSERT INTO tasks (title, description, status_id, user_id)
                    VALUES ('{task}', 'New Task', 1, 
                    (SELECT id FROM users WHERE fullname = '{name}'));"""
        sql_update(conn, request)
        print("Task updated.")

        # Отримати всі завдання, які ще не завершено.
        print("All unfinished tasks")
        request = "SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'completed')"
        print(sql_request(conn, request))

        # Видалити конкретне завдання.
        print("Delete task by id")
        task = input('Enter task id: ')
        request = f"DELETE FROM tasks WHERE id = {task}"
        sql_update(conn, request)
        print(f"Task '{task}' successfully deleted")

        # Знайти користувачів з певною електронною поштою.
        print("Search user by e-mail")
        email = input('Enter e-mail pattern: ')
        request = f"SELECT * FROM users WHERE email LIKE '%{email}%'"
        print(sql_request(conn, request))

        # Оновити ім'я користувача.
        print("User name update")
        old_name = input('Enter full name: ')
        new_name = input('Enter new full name: ')
        request = f"UPDATE users SET fullname = '{new_name}' WHERE fullname = '{old_name}'"
        sql_update(conn, request)
        print(f"New name: {new_name}")

        # Отримати кількість завдань для кожного статусу.
        print("Count by status")
        request = ("""SELECT COUNT(status_id) as task_count, status_id
                   FROM tasks
                   GROUP BY status_id;""")
        print(sql_request(conn, request))

        # Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
        print("Tasks for users with email domain @example.com")
        request = ("""SELECT tasks.*
                   FROM tasks
                   JOIN users ON tasks.user_id = users.id
                   WHERE users.email LIKE '%@example.com';""")
        print(sql_request(conn, request))

        # Отримати список завдань, що не мають опису.
        print("Tasks that have no description")
        request = "SELECT * FROM tasks WHERE description IS NULL OR description = '';"
        print(sql_request(conn, request))

        # Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
        print("List of users and tasks with status 'in progress'")
        request = ("""SELECT users.fullname, tasks.title
                   FROM users
                   JOIN tasks ON users.id = tasks.user_id
                   JOIN status ON tasks.status_id = status.id
                   WHERE status.name = 'in progress';""")
        print(sql_request(conn, request))

        # Отримати користувачів та кількість їхніх завдань.
        print("Users and number of tasks")
        request = ("""SELECT users.fullname, COUNT(*)
                   FROM users
                   LEFT JOIN tasks ON tasks.user_id = users.id
                   GROUP BY users.fullname""")
        print(sql_request(conn, request))

