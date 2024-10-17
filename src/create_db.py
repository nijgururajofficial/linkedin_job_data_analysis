import sqlite3
import pandas as pd

df = pd.read_csv('../data/raw/linkedin_job_postings.csv')  

conn = sqlite3.connect('../data/database/linkedin_jobs.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS job_postings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    location TEXT
)
''')

for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO job_postings (job_title, company, location)
        VALUES (?, ?, ?)
    ''', (row['Job Title'], row['Company'], row['Location']))

conn.commit()
conn.close()

print("Data successfully stored in SQLite database.")
