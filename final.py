
def get_user_input():
    print("Hi! Welcome to movie finder! We'll take your age, favorite genres, and the streaming services you have and give you movie info and recommendations!")
    age = -1
    genre = ""
    while age < 0 or age > 100:
        age = input(print("How old are you? (0-100)"))
    print("We can show you action, comedy, romance, etc")
    genre = input(print("What genres do you like? Please enter as comma seperated list ie 'action, comedy'")).split(',')
    print("We can show you movies on hulu, netflix, max, etc")
    services = input(print("Which of these services do you have? Please enter as a comma seperated list ie 'hulu, max'")).split(',')

#def collect_data_omdb():

#def collect_data_watchmode():

# def filter_by_age(age):
#filter movies based on rating ie pg, pg13, r 
#return list of movies that fit the age rating 

# def filter_by_genre():
#filter movies based on genres 
# returns list of movie names with genres that align 

# def filter_by_service():
# makes a new list of movie titles that are on both genre and age 
#returns list of movie names that are on the services the user has 

# def filter_by_ratings()
# returns top 10 movies that match everything 
# has a bar chart that shows the ratings for the movies 

# get_info():
# gives info on movies like rating, poster, genre, streaming services, year made, 
# country, etc 

def main():
    info = get_user_input() 
    #run all of the filtering 
    #ask if user wants more info on any of the movies
    #output data for that movie 


if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)