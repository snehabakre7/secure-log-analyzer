import mysql.connector

# ==============================
# DATABASE CONNECTION
# ==============================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="logdb"
)

cursor = conn.cursor()

print("\n==== SECURITY REPORT ====\n")

# ==============================
# STEP 1: BRUTE FORCE DETECTION
# ==============================
cursor.execute("""
SELECT user, ip, COUNT(*) as attempts
FROM logs
WHERE status = 'FAILED'
GROUP BY user, ip
HAVING attempts >= 3
""")

results = cursor.fetchall()

if results:
    print("Brute Force Attacks Detected:\n")
    for row in results:
        print(f"User: {row[0]} | IP: {row[1]} | Attempts: {row[2]}")
else:
    print("No brute force attacks detected.\n")


# ==============================
# STEP 2: SUSPICIOUS IP DETECTION
# ==============================

# FIX: defined outside condition
trusted_ips = ["192.168.1.10", "10.0.0.5"]

cursor.execute("SELECT DISTINCT ip FROM logs")
ips = cursor.fetchall()

print("\n Suspicious IPs:\n")

found = False
for (ip,) in ips:
    if ip not in trusted_ips:
        print(ip)
        found = True

if not found:
    print("No suspicious IPs found.")


# ==============================
# STEP 3: FAILED LOGIN COUNT
# ==============================
cursor.execute("SELECT COUNT(*) FROM logs WHERE status='FAILED'")
total_failed = cursor.fetchone()[0]

print(f"\nTotal Failed Login Attempts: {total_failed}")


# ==============================
# CLEANUP
# ==============================
conn.close()

print("\nAnalysis Complete.\n")
