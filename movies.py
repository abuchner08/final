import requests 
import sqlite3
import json 
from apikeymovies import key

def get_data(key):
    moviels = ["Barbie", "Avatar", "Smile", "The Game", "Dodgeball", "Love Actually", "It", "Home Alone", "Room", "The Notebook", 
               "Mean Girls", "Clueless", "Die Hard", "Titanic", "Epic", "Mummy", "Schndler's List", "Dead Poets Society", 
               "Jaws", "Jerry Maguire", "Wonder", "Bring It On", "Lost", "Ghost", "Fight Club"]
    ls = []
    for movie in moviels:
        params = {'t' : movie, 'apikey' : key}
        response = requests.get(f"http://www.omdbapi.com/?", params=params)
        data = response.json()
        ls.append(data)
    #print(ls)
    return ls

def set_up_table(data):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
    id TEXT PRIMARY KEY,
    title TEXT, 
    boxoffice INTEGER
    )
    ''')
    #print(data)
    for movie in data:
        #print(movie)
        id = movie.get("imdbID")
        title = movie.get("Title")
        Bo = movie.get("BoxOffice", "").replace("$","").replace(",","")
        print(id, title, Bo)

        try:
            cursor.execute('''
            INSERT INTO movies (id, title, boxoffice) VALUES (?,?,?)
            ''', (id, title, int(Bo)))
        except:
            print("error")

    conn.commit()

def main():
    set_up_table(get_data(key))

main()