import requests
import json

def get_apikey(filename):
    f = open(filename, 'r')
    key = f.read().strip()
    return key
   
def get_user_input():
    print("Hi! Welcome to movie finder! We'll take your age, favorite genres, and the streaming services you have and give you movie info and recommendations!")
    age = -1
    genre = ""
    while age < 0 or age > 100:
        age = input(print("How old are you? (0-100)"))
    print("We can show you action, comedy, romance, etc")
    genre = input(print("What genres do you like? Please enter as comma seperated list ie 'action, comedy'")).split(',')
    print("We can show you movies on max, abc, hulu, netflix, disney+, hbo")
    services = input(print("Which of these services do you have? Please enter as a comma seperated list ie 'max, vudu, hulu, spectrum'")).split(',')

#def collect_data_omdb():

def collect_data_watchmode():
    apikey = get_apikey('apikey.txt')
    res = requests.get(f"https://api.watchmode.com/v1/title/345534/details/?apiKey={apikey}")
    data = res.json()
    print(data)

# def filter_by_age(age):
#filter movies based on rating ie pg, pg13, r 
#return list of movies that fit the age rating 

# def filter_by_genre():
#filter movies based on genres 
# returns list of movie names with genres that align 

# def filter_by_service():
# makes a new list of movie titles that are on both genre and age 
#returns list of movie names that are on the services the user has 

#def get_average_rating(movie)
# gets the average rating from all the different rating sites 

'''
def filter_by_ratings(age, genre, service):
    common = []
    for movie in service:
        if movie in age and movie in genre:
            common.append(movie)
    for movies in common:
        # calculate the rating 
        # make list of tuples with title and rating 
        # sort by max rating 
    #return top 10 or however many there are 
    if len(common) == 0:
        return service[0:10]
'''
# takes in the three lists that have already been made and return top movies that are in all three
# returns top 10 movies or less if thats all there is that match everything 
# has a bar chart that shows the ratings for the movies 

# get_info():
# gives info on movies like rating, poster, genre, streaming services, year made, 
# country, etc 

def main():
    #info = get_user_input() 
    collect_data_watchmode()

    #run all of the filtering 
    #ask if user wants more info on any of the movies
    #output data for that movie 


if __name__ == "__main__":
    main()
    #unittest.main(verbosity=2)