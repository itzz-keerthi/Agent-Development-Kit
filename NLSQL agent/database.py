import sqlite3

# Connect to SQLite database (this creates the database file if it doesn't exist)
conn = sqlite3.connect('employees.db')

# Create a cursor to execute SQL commands
c = conn.cursor()

# Create the employees table
c.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone_number TEXT,
        hire_date TEXT,
        job_title TEXT,
        salary REAL,
        department TEXT
    )
''')

# Insert sample data
c.executemany('''
    INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_title, salary, department)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2022-01-15', 'Software Engineer', 85000.00, 'Engineering'),
    ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '2021-07-23', 'Data Analyst', 75000.00, 'Data Science'),
    ('Robert', 'Johnson', 'robert.johnson@example.com', '555-123-4567', '2019-09-05', 'Project Manager', 95000.00, 'Operations'),
    ('Emily', 'Davis', 'emily.davis@example.com', '444-321-6789', '2020-03-11', 'UX Designer', 72000.00, 'Design'),
    ('Michael', 'Wilson', 'michael.wilson@example.com', '666-987-6543', '2021-12-30', 'HR Manager', 78000.00, 'Human Resources')
])

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'employees.db' created and data inserted.")
