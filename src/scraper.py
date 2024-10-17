import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
import os

base_url = "https://www.linkedin.com/jobs/search?keywords=Database%20Administrator&location=United%20States"

headers = {"User-Agent": "Mozilla/5.0"}

job_postings = []
unique_jobs = set()  

jobs_per_page = 25
max_pages = 500

response = requests.get(base_url, headers=headers)
print(response.status_code)

for page in range(0, max_pages * jobs_per_page, jobs_per_page):
    url = f"{base_url}&start={page}"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_cards = soup.find_all('div', class_='base-search-card__info')  # Job card containing all info
    
    for card in job_cards:
        job_title = card.find('h3', class_='base-search-card__title').get_text(strip=True)
        company = card.find('h4', class_='base-search-card__subtitle').get_text(strip=True)
        location = card.find('span', class_='job-search-card__location').get_text(strip=True)
        
        job_data = (job_title, company, location)
        
        # Check if the job is already added
        if job_data not in unique_jobs:
            unique_jobs.add(job_data)
            job_postings.append({
                "Job Title": job_title,
                "Company": company,
                "Location": location
            })
    
    time.sleep(2)  # Sleep to avoid getting blocked by LinkedIn

print(f"Total unique job postings scraped: {len(job_postings)}")

# Save to JSON
with open('../data/raw/linkedin_job_postings.json', 'w') as f:
    json.dump(job_postings, f, indent=4)

# Save to CSV
df = pd.DataFrame(job_postings)
csv_file_path = '../data/raw/linkedin_job_postings.csv'

if os.path.exists(csv_file_path):
    existing_jobs_df = pd.read_csv(csv_file_path)
    updated_jobs_df = pd.concat([existing_jobs_df, df], ignore_index=True)
    updated_jobs_df.drop_duplicates(subset=['Job Title', 'Company', 'Location'], keep='last', inplace=True)
else:
    updated_jobs_df = df

updated_jobs_df.to_csv(csv_file_path, index=False)
