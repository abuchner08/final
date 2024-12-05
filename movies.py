import requests 
import sqlite3
import json 

def get_api_key(file):
    f = open(file, 'r')
    key = f.read().strip()
    return key 

def get_data():
    apikey = get_api_key("apikeymovies")
    response = requests.get(f"http://www.omdbapi.com/?apikey={apikey}&")
    data = json.load(response.text)

    return data

def set_up_table(data):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT, 
    boxoffice INT
    )
    ''')
    for movie in data:
        id = movie["imdbID"]
        title = movie["Title"]
        Bo = movie["BoxOffice"]

        cursor.execute('''
        INSERT INTO movies (id, title, Bo) VALUES (?,?,?)
        ''', (id, title, Bo))

    conn.commit()

def main():
    data = get_data()
    set_up_table(data)

main()