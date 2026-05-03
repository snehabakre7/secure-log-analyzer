# Secure Log Analyzer (Python + MySQL)

## Project Overview

This project is a cybersecurity-focused log analysis tool that examines authentication logs to detect potential security threats such as brute-force attacks and suspicious IP activity.

It simulates a basic Security Operations Center (SOC) workflow where logs are monitored and analyzed to identify unauthorized access attempts.

---

## Features

* Detects brute-force login attempts based on repeated failures
* Identifies suspicious IP addresses not present in a trusted list
* Counts total failed login attempts
* Generates a structured and readable security report
* Includes sample data generation for testing

---

## Technologies Used

* Python
* MySQL
* SQL

---

## Project Files

* analyzer.py            # Main script for log analysis
* generator.py           # Generates sample log data
* logs.sql               # Database setup and sample data
* README.md              # Project documentation
* database base.png      # Screenshot of the table generated 

---

## How It Works

The system connects to a MySQL database named `logdb` and reads login records from the `logs` table. It performs brute-force detection by identifying multiple failed login attempts from the same user and IP address. It also compares all IP addresses against a predefined trusted list to flag suspicious entries. The results are displayed as a structured report in the terminal.

---

## Database Setup

Open MySQL:

```sql
mysql -u root -p
```

Run the SQL file:

```sql
source path/to/logs.sql;
```

Example:

```sql
source C:/Users/YourName/Desktop/log-analyzer-mysql/logs.sql;
```

---

## How to Run the Project

Run the data generator (optional):

```bash
python generator.py
```

Run the analyzer:

```bash
python analyzer.py
```

---

## Sample Output

<img width="1360" height="660" alt="image" src="https://github.com/user-attachments/assets/554e9d2c-ee49-495d-a2cd-b76a39cbf331" />

---

## Security Note

Do not store real database credentials in the source code. Use environment variables for better security practices.

---

## Use Case

This project demonstrates how cybersecurity professionals monitor logs, detect suspicious activity, and identify attack patterns such as brute-force attempts.

---

## Future Improvements

* Add real-time monitoring
* Integrate alert system
* Build a web dashboard using Flask
* Add time-based log filtering
* Enhance anomaly detection

---

## Learning Outcomes

* Understanding log analysis in cybersecurity
* Working with databases using Python
* Writing SQL queries for data analysis
* Identifying common attack patterns

---

## Certification

This project was developed as part of the "Foundations of Cybersecurity" course from the Google Cybersecurity Professional Certificate. It reflects the practical application of concepts such as log analysis, SQL querying, and basic task automation using Python.

---

## Author

This project was developed as a beginner-level cybersecurity project using Python and MySQL.

---
