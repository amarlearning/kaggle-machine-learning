## 2. Parsing the File ##

weather_data = []

file = open("la_weather.csv", "r")
data = file.read().split("\n")

for i in data:
    weather_data.append(i.split(","))


## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for data in weather_data:
    weather.append(data[1])

## 4. Counting the Items in a List ##

count = 0

for i in weather:
    count = count + 1

count == len(weather)

## 5. Removing the Header ##

new_weather = weather[1:366]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for i in weather_types:
    weather_type_found.append(i in new_weather)