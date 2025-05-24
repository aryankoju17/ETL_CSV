import csv
import pymysql

# Connect to MySQL database
mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

cursor = mydb.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS testcsv (
    name VARCHAR(255),
    age INT,
    gender VARCHAR(20)
);
''')

# Read CSV file and insert data
with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Use DictReader if CSV has headers

    for row in reader:
        cursor.execute(
            'INSERT INTO testcsv (names, age, gender) VALUES (%s, %s, %s)',
            (row['name'], row['age'], row['gender'])
        )

mydb.commit()
cursor.close()
mydb.close()

print("CSV data loaded successfully!")
