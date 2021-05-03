import csv

data = []
# This is the list variable on which each row a dictionary representing each a line of the csv file
# Each line of data contains a new row of information
# 'filename' has to be dynamic as it is equal to the file name that the user uploaded
# ('enron-v1.csv' is currently a placeholder)

filename = 'enron-v1.csv'
with open('csv_files/{}'.format(filename)) as File:
    reader = csv.DictReader(File)
    for row in reader:
        data.append(row)    # PS, if you think there is a better way to structure this data, feel free to change

amount_keys = len(data[0].keys())  # Amount of items per row in the csv file

# Here we need to define abstract variables about the data which can be used for different formats of data
