import mysql.connector
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="logdb"
)

cursor = conn.cursor()

users = ["user1", "user2", "admin"]
ips = ["192.168.1.10", "10.0.0.5", "45.23.12.90", "172.16.0.3", "8.8.8.8"]
statuses = ["SUCCESS", "FAILED"]

time = datetime.now()

for _ in range(50):
    time += timedelta(seconds=random.randint(1, 60))
    user = random.choice(users)
    ip = random.choice(ips)
    status = random.choices(statuses, weights=[0.4, 0.6])[0]

    cursor.execute(
        "INSERT INTO logs (timestamp, status, user, ip) VALUES (%s, %s, %s, %s)",
        (str(time), status, user, ip)
    )

# Simulate brute force attack
for _ in range(5):
    cursor.execute(
        "INSERT INTO logs (timestamp, status, user, ip) VALUES (%s, %s, %s, %s)",
        (str(time), "FAILED", "admin", "45.23.12.90")
    )

conn.commit()
conn.close()

print("Logs inserted successfully!")