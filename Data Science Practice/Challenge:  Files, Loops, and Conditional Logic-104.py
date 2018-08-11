## 3. Read the File Into a String ##

file = open("dq_unisex_names.csv", "r")

names = file.read()


## 4. Convert the String to a List ##

first_five = []
f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split("\n")

for i in range(5):
    first_five.append(names_list[i])

print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

nested_list = []

f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split('\n')

for name in names_list:
    nested_list.append(name.split(","))

## 6. Convert Numerical Values ##

numerical_list = []

for data in nested_list:
    new_list = []
    name = data[0]
    number = float(data[1])
    new_list = [name, number]
    numerical_list.append(new_list)

## 7. Filter the List ##

thousand_or_greater = []

for data in numerical_list:
    if data[1] >= 1000:
        thousand_or_greater.append(data[0])

print(data[0:10])