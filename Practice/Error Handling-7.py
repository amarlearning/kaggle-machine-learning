## 2. Sets ##

gender = []
for row in legislators:
    gender.append(row[3])

gender = set(gender)


## 3. Exploring the Dataset ##

party = set()
for row in legislators:
    party.add(row[6])

print(party)
print(legislators)

## 4. Missing Values ##

for row in legislators:
    if row[3] == '':
        row[3] = "M"

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    date_of_birth = row[2].split("-")
    birth_years.append(date_of_birth[0])

## 6. Try/except Blocks ##

try:
    value = float("hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    value = int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##

birth_year = []

for row in legislators:
    try:
        birth_year = int(row[2].split("-")[0])
    except Exception:
        birth_year= 0
    row.append(birth_year)

print(legislators)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]