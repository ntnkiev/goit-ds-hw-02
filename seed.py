from faker import Faker
import psycopg2
import random
from connect import connection_parameters

# Налаштування Faker для генерації даних
fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(**connection_parameters)
cur = conn.cursor()

# заповнення таблиці status
cur.execute("INSERT INTO status (id, name) VALUES (1, 'new'), (2, 'in progress'), (3, 'completed');")

# генерація даних для таблиці users
for i in range(100):  # Заповнення користувачів
    fullname = fake.name()
    email = fake.unique.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# генерація даних для таблиці tasks
cur.execute("SELECT id FROM users")
users_ids = cur.fetchall()
cur.execute("SELECT id FROM status")
status_ids = cur.fetchall()

for i in range(200):  # Заповнення завдань
    title = fake.sentence(nb_words=2)
    description = fake.text()
    status_id = random.choice(status_ids)[0]
    user_id = random.choice(users_ids)[0]
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

# Збереження змін та закриття з'єднання
conn.commit()
cur.close()
conn.close()
