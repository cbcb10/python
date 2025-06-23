import pyodbc
import pandas as pd
import schedule
import time
import datetime
import unittest

# Define the connection details for the SQL Server
server = 'my_server'
database = 'my_database'
username = 'my_username'
password = 'my_password'

# Function to create a connection to the SQL Server
def create_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    return conn

# Function to extract the columns with the highest total sum
def get_top_two_columns():
    conn = create_connection()
    query = 'SELECT * FROM my_table'
    df = pd.read_sql(query, conn)
    top_two_columns = df.sum().nlargest(2).index
    result = df[top_two_columns]
    print(result)
    return result

# Function to schedule the code to run daily at 12:00 PM
def schedule_daily_job():
    schedule.every().day.at("12:00").do(get_top_two_columns)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Function to schedule the code to run every 10 days starting from a specific date
start_date = datetime.date(2023, 1, 1)
def schedule_ten_day_job():
    def job():
        today = datetime.date.today()
        if (today - start_date).days % 10 == 0:
            get_top_two_columns()
    while True:
        job()
        time.sleep(86400)  # Wait for one day

# Test group
class TestDatabaseFunctions(unittest.TestCase):

    def test_top_two_columns(self):
        conn = create_connection()
        query = 'SELECT * FROM my_table'
        df = pd.read_sql(query, conn)
        top_two_columns = df.sum().nlargest(2).index
        self.assertEqual(len(top_two_columns), 2)
        self.assertTrue(all(col in df.columns for col in top_two_columns))

if __name__ == '__main__':
    # Run tests
    unittest.main(exit=False)
    
    # Run the schedulers
    # Note: You can only run one scheduler at a time
    # schedule_daily_job()
    # schedule_ten_day_job()
