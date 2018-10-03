import csv

with open("eggs.csv", "w",newline='') as file:
    data = csv.writer(file,delimiter='',quotchar='',quoting=csv.QUOTE_MINIMAL)

