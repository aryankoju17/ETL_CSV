import psycopg2
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=""
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS People (
    name VARCHAR(255),
    age INTEGER,
    gender VARCHAR(20)
);
''')
conn.commit()

# Read CSV and Insert into DB
with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Automatically maps header names to values
    for row in reader:
        cursor.execute('''
        INSERT INTO People (name, age, gender)
        VALUES (%s, %s, %s);
        ''', (row['name'], row['age'], row['gender']))

conn.commit()
print("CSV data loaded successfully!")

# Display inserted data
cursor.execute("SELECT * FROM People;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()

# import psycopg2
# import csv

# # STEP 1: Connect to the default database
# conn = psycopg2.connect(
#     host="localhost",
#     database="postgres",  # default admin DB
#     user="postgres",
#     password="your_password_here"  # replace with your actual password
# )
# conn.autocommit = True  # allow CREATE DATABASE command
# cursor = conn.cursor()

# # STEP 2: Create new database if it doesn't exist
# cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'etl_db';")
# exists = cursor.fetchone()

# if not exists:
#     cursor.execute("CREATE DATABASE etl_db;")
#     print("Database 'etl_db' created successfully!")

# # Close connection to default DB
# cursor.close()
# conn.close()

# # STEP 3: Connect to the new database
# conn = psycopg2.connect(
#     host="localhost",
#     database="etl_db",  # newly created DB
#     user="postgres",
#     password="your_password_here"
# )
# cursor = conn.cursor()

# # STEP 4: Create table if not exists
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Person (
#     name VARCHAR(255),
#     age INTEGER,
#     gender VARCHAR(20)
# );
# ''')
# conn.commit()
# print("Table 'Person' is ready!")

# # STEP 5: Read CSV and Insert data
# with open('input.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         cursor.execute('''
#         INSERT INTO Person (name, age, gender)
#         VALUES (%s, %s, %s);
#         ''', (row['name'], row['age'], row['gender']))

# conn.commit()
# print("CSV data loaded successfully!")

# # STEP 6: Show inserted data
# cursor.execute("SELECT * FROM Person;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Close everything
# cursor.close()
# conn.close()
