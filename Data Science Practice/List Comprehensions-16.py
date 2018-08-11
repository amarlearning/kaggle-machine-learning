## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [(price * 2) for price in apple_prices]
apple_prices_lowered = [(price - 100) for price in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for row in legislators:
    if row[3] == 'F' and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for value in values:
    if value is not None and value > 30:
        checks.append(True)
    else:
        checks.append(False)

## 8. Highest Female Name Count ##

max_value = None

for keys in name_counts:
    count = name_counts[keys]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for key, value in plant_types.items():
    print(key, value)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for key, value in name_counts.items():
    if value == 2:
        top_female_names.append(key)

## 11. Finding the Most Common Male Names ##

def item_list(d_col, g_col, y_col):
    male_name_counts = {}
    for row in legislators:
        if row[g_col] == "M" and row[y_col] > 1740:
            if row[d_col] in male_name_counts:
                male_name_counts[row[d_col]] += 1
            else:
                male_name_counts[row[d_col]] = 1                
    return male_name_counts

def highest_value(male_name_counts):
    highest_male_count = None
    for _, value in male_name_counts.items():
        if highest_male_count is None or value > highest_male_count:
            highest_male_count = value
    return highest_male_count
    
def top_names(male_name_counts, highest_male_count):
    top_male_names = []
    for key, value in male_name_counts.items():
        if value == highest_male_count:
            top_male_names.append(key)
            
    return top_male_names

            
male_name_counts = item_list(1, 3, 7)
highest_male_count = highest_value(male_name_counts)
top_male_names = top_names(male_name_counts, highest_male_count)
