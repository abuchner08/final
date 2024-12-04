import requests 
import sqlite3
import json 
import os
#make database with movie id, title, and box office money 

def get_api_key(file):
    f = open(filename, 'r')
    key = f.read().strip()
    return key 

def get_data():
    apikey = get_api_key("apikeymovies")
    reponse = requests.get(f"http://www.omdbapi.com/?apikey={apikey}&")
    data = response.json()

def set_up_table(data):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    movie_data = []
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT, 
    boxoffice INT
    )
    ''')
    for movie in data:
        #id = movie[]
        title = movie["Title"]
        Bo = movie["BoxOffice"]

        cursor.execute('''
        INSERT INTO movies (id, title, Bo) VALUES (?,?,?)
        ''', (id, title, Bo))

    conn.commit()