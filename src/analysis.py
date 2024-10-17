import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

conn = sqlite3.connect('../data/database/linkedin_jobs.db')

query = "SELECT * FROM job_postings"
df = pd.read_sql_query(query, conn)

conn.close()

print("Data Info:")
print(df.info())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

df.fillna('Not Available', inplace=True)

df_filtered = df[df['location'] != 'United States']

job_by_location = df_filtered['location'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=job_by_location.values, y=job_by_location.index)
plt.title('Top 10 Job Locations')
plt.xlabel('Number of Jobs')
plt.ylabel('Location')
plt.show()

top_companies = df_filtered['company'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_companies.values, y=top_companies.index)
plt.title('Top 10 Hiring Companies')
plt.xlabel('Number of Jobs')
plt.ylabel('Company')
plt.show()

locations_text = ' '.join(df_filtered['location'].dropna().astype(str))
wordcloud_locations = WordCloud(width=800, height=400, background_color='white').generate(locations_text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_locations, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Job Locations')
plt.show()

companies_text = ' '.join(df_filtered['company'].dropna().astype(str))
wordcloud_companies = WordCloud(width=800, height=400, background_color='white').generate(companies_text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_companies, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Hiring Companies')
plt.show()

titles_text = ' '.join(df_filtered['job_title'].dropna().astype(str))  # Combine all job titles into a single string
wordcloud_titles = WordCloud(width=800, height=400, background_color='white', collocations=False).generate(titles_text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_titles, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Job Titles')
plt.show()
