import sqlite3
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from wordcloud import WordCloud
import numpy as np
import base64
import io
import dash_bootstrap_components as dbc

# Connect to SQLite database
conn = sqlite3.connect('../data/database/linkedin_jobs.db')
query = "SELECT * FROM job_postings"
df = pd.read_sql_query(query, conn)
conn.close()

# Clean data (ignore 'United States' in location)
df = df[~df['location'].str.contains("United States")]

# Create Word Cloud for Job Titles
wordcloud_titles = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['job_title']))
buffer_titles = io.BytesIO()
wordcloud_titles.to_image().save(buffer_titles, format='PNG')
buffer_titles.seek(0)
img_titles_str = base64.b64encode(buffer_titles.getvalue()).decode()

# Create Word Cloud for Locations
wordcloud_locations = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['location']))
buffer_locations = io.BytesIO()
wordcloud_locations.to_image().save(buffer_locations, format='PNG')
buffer_locations.seek(0)
img_locations_str = base64.b64encode(buffer_locations.getvalue()).decode()

# Create Word Cloud for Companies
wordcloud_companies = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['company']))
buffer_companies = io.BytesIO()
wordcloud_companies.to_image().save(buffer_companies, format='PNG')
buffer_companies.seek(0)
img_companies_str = base64.b64encode(buffer_companies.getvalue()).decode()

# Create Top 10 Locations Chart
top_locations = df['location'].value_counts().head(10).reset_index()
top_locations.columns = ['Location', 'Number of Jobs']
location_fig = px.bar(top_locations, x='Number of Jobs', y='Location', title='Top 10 Job Locations', orientation='h', color='Number of Jobs')

# Create Top 10 Companies Chart
top_companies = df['company'].value_counts().head(10).reset_index()
top_companies.columns = ['Company', 'Number of Jobs']
company_fig = px.bar(top_companies, x='Number of Jobs', y='Company', title='Top 10 Hiring Companies', orientation='h', color='Number of Jobs')

# Create Most Used Keywords in Job Titles Chart
all_keywords = ' '.join(df['job_title']).split()
keyword_counts = pd.Series(all_keywords).value_counts().head(10).reset_index()
keyword_counts.columns = ['Keyword', 'Frequency']
keyword_fig = px.bar(keyword_counts, x='Frequency', y='Keyword', title='Most Used Keywords in Job Titles', orientation='h', color='Frequency')

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("LinkedIn Job Postings Dashboard", className="text-center my-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=location_fig), md=6),
        dbc.Col(dcc.Graph(figure=company_fig), md=6),
    ]),
    
    dbc.Row([
        dbc.Col(html.Div([
            html.H2("Word Cloud for Job Titles", className="text-center"),
            html.Img(src='data:image/png;base64,{}'.format(img_titles_str), style={'width': '100%', 'height': 'auto', 'border': '1px solid #e6e6e6', 'border-radius': '5px'})
        ]), md=4),
        
        dbc.Col(html.Div([
            html.H2("Word Cloud for Locations", className="text-center"),
            html.Img(src='data:image/png;base64,{}'.format(img_locations_str), style={'width': '100%', 'height': 'auto', 'border': '1px solid #e6e6e6', 'border-radius': '5px'})
        ]), md=4),
        
        dbc.Col(html.Div([
            html.H2("Word Cloud for Companies", className="text-center"),
            html.Img(src='data:image/png;base64,{}'.format(img_companies_str), style={'width': '100%', 'height': 'auto', 'border': '1px solid #e6e6e6', 'border-radius': '5px'})
        ]), md=4),
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=keyword_fig), md=12),
    ]),
    
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=False)
