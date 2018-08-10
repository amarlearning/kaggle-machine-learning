## 1. Overview ##

movie_data = []
movie_data_string = open("movie_metadata.csv", "r").read()
movie_data_list = movie_data_string.split("\n")

for i in movie_data_list:
    movie_data.append(i.split(","))

print(movie_data[1:5])

## 3. Writing Our Own Functions ##



def first_elts(movie_data):
    movie_names = []
    for movie in movie_data:
        movie_names.append(movie[0])
    return movie_names

movie_names = first_elts(movie_data)
print(movie_names[1:6])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(wonder_woman):
    if wonder_woman[6] == "USA":
        return True
    else:
        return False


wonder_woman_usa = is_usa(wonder_woman)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def index_equals_str(input_lst, string, index):
    if input_lst[index] == string:
        return True
    else:
        return False

wonder_woman_in_color = index_equals_str(wonder_woman,'Color', 2)

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt


def feature_counter(movie_data, String, col, header_row = False):
    usa_movie_list = []
    for movie in movie_data:
        bool_movie = index_equals_str(movie, col, String)
        if bool_movie:
            usa_movie_list.append(movie)

    return counter(usa_movie_list, header_row)

num_of_us_movies = feature_counter(movie_data, "USA", 6, False)
            

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst, index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(movie_data):
    dictionary = {}
    num_japan_films = feature_counter(movie_data, 6, "Japan", True)
    num_color_films = feature_counter(movie_data, 2, "Color", True)
    num_films_in_english = feature_counter(movie_data, 5, "English", True)

    dictionary["japan_films"] = num_japan_films
    dictionary["color_films"] = num_color_films
    dictionary["films_in_english"] = num_films_in_english

    return dictionary

summary = summary_statistics(movie_data)