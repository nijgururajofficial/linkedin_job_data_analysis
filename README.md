### README Documentation

# LinkedIn Job Data Analysis Project

This project is aimed at scraping job data from LinkedIn, storing it in a SQLite database, performing exploratory data analysis (EDA), and visualizing the insights through an interactive dashboard.

## Folder Structure
```
├── dashboards/ 
│   ├── app.py                            # Dashboard application built using Dash and Plotly 
├── data/
│   ├── database  
│   │   ├── linkedin_jobs.db               # SQLite database storing the job data 
│   ├── raw  
│   │   ├── linkedin_job_postings.db       # Raw database for job postings (alternative)
│   │   ├── linkedin_job_postings.json     # Raw JSON file with scraped job data 
├── notebooks/                       
│   ├── 01_data_scraping.ipynb             # Notebook for web scraping LinkedIn job postings 
│   ├── 02_create_db.ipynb                 # Notebook for creating the SQLite database 
│   ├── 03_analysis.ipynb                  # Notebook for exploratory data analysis 
├── src/                             
│   ├── scraper.py                        # Python script for web scraping 
│   ├── create_db.py                      # Python script for creating and storing data in the database 
│   ├── analysis.py                       # Python script for data analysis 
├── requirements.txt                     # Dependencies required to run the project 
└── README.md                            # Project documentation
```

## Project Workflow

### 1. **Data Scraping (01_data_scraping.ipynb / scraper.py)**
   - Scrapes job postings from LinkedIn.
   - Extracted fields include job titles, company names, and job locations, excluding generic locations like "United States."

### 2. **Database Creation (02_create_db.ipynb / create_db.py)**
   - Stores the scraped job data into a local SQLite database (`linkedin_jobs.db`).
   - Utilizes `sqlite3` for efficient storage and query handling.

### 3. **Data Analysis (03_analysis.ipynb / analysis.py)**
   - Performs exploratory data analysis (EDA) to discover insights.
   - Generates word clouds and bar charts to visualize the following:
     - Top 10 job locations.
     - Top 10 hiring companies.
     - Most frequently used keywords in job titles.

### 4. **Dashboard (app.py)**
   - Interactive web dashboard using Dash and Plotly.
   - Displays:
     - Word clouds for job titles, locations, and companies.
     - Bar charts for top locations, top companies, and most-used keywords in job titles.

## How to Run the Project

### Prerequisites:
- Python 3.8+
- Install dependencies by running:
  ```bash
  pip install -r requirements.txt
  ```

### Steps to Run:
1. **Scrape Data:**
   Run the scraping script to fetch LinkedIn job postings:
   ```bash
   python src/scraper.py
   ```

2. **Create Database:**
   Store the scraped data in the SQLite database:
   ```bash
   python src/create_db.py
   ```

3. **Data Analysis:**
   Perform exploratory data analysis:
   ```bash
   python src/analysis.py
   ```

4. **Launch Dashboard:**
   Start the dashboard to visualize the analysis:
   ```bash
   python dashboards/app.py
   ```

## Key Visualizations:
- **Word Clouds**:
  - Word clouds for job titles, companies, and locations help reveal the most frequent words.
- **Bar Charts**:
  - Visualize top 10 job locations, hiring companies, and popular keywords in job titles.


Feel free to customize and enhance the project as per your requirements!
