## 2. Defining the Dataset Class ##

class Dataset:
    
    def __init__(self):
        self.type = "csv"
        
        
dataset = Dataset()
dataset.type

## 3. Passing Additional Arguments to the Initializer ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.type = "csv"
        self.data = data
        
f = open("nfl.csv", "r")
nfl_data = list(csv.reader(f))

nfl_dataset = Dataset(nfl_data)

dataset_data = nfl_dataset.data

## 4. Adding Additional Behavior ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        
    # Your method goes here
    def print_data(self, num_rows):
        print(self.data[:num_rows])
        
nfl_dataset = Dataset(nfl_data)

nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        self.header = data[0]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

## 6. Grabbing Column Data ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    def column(self, label):
        sample_list = []
        try:
            self.index = self.header.index(label)
        except:
            return None
        
        for data in self.data:
            sample_list.append(data[self.index])
        return sample_list

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

## 7. Count Unique Method ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    # Add your count unique method here
    def count_unique(self, label):
        column_list = self.column(label)
        unique_results = set(column_list)
        return len(unique_results)
    
nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique("year")

## 8. Make Objects Human Readable ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # Add the special method here
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count
    
    def __str__(self):
        return str(self.data[0:10])

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)