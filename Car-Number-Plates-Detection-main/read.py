# Python program to demonstrate
# writing to CSV


import csv

# field names
fields = ["Plate Number"]

# data rows of csv file
rows = ["result"]

# name of csv file
filename = "number_plate_data.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
