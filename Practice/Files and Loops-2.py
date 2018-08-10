## 1. Opening Files ##

f = open("crime_rates.csv", "r")

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
# print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
# print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
for i in range(5):
    print(rows[i])

## 5. Practice - Loops ##

ten_rows = rows[0:10]

for row in ten_rows:
    print(row)

## 7. Practice - Splitting Elements in a List ##

final_data = []
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

for row in rows:
    split_data = row.split(",")
    final_data.append(split_data)

print(final_data[0:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

cities_list = []
for element in five_elements:
    cities_list.append(element[0])

print(cities_list)

## 9. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)

cities_list = []
for cities in final_data:
    cities_list.append(cities[0])

## 10. Challenge ##

int_crime_rates = []
f = open('crime_rates.csv', 'r')
rows = f.read().split('\n')


for row in rows:
    int_crime_rates.append(int(row.split(",")[1]))