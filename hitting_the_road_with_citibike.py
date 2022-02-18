# question: How many Citi Bike rides each day are taken by
# "subscribers" versus "customers"?
# answer: Choose a single day of rides to examine.
# the dataset used for this exercise was generated from the original
# Citi Bike system data found here:https://s3.amazonaws.com/tripdata/index.html
# filename: 202009-citibike-tripdata.csv.zip
# program Outline:
# 1. read in the data file: 202009CitibikeTripdataExample.csv
# 2. create variables to count: subscribers, customers, and other
# 3. for each row in the file:
# a. If the "User Type" is "Subscriber," add 1 to "subscriber_count"
# b. If the "User Type" is "Customer," add 1 to "customer_count"
# c. Otherwise, add 1 to the "other" variable
# 4. print out my results

# import the `csv` library 
import csv
# open the `202009CitibikeTripdataExample.csv` file in read ("r") mode
# this file should be in the same folder as our Python script or notebook
source_file = open("202009CitibikeTripdataExample.csv","r")
# pass our `source_file` as an ingredient to the `csv` library's
# DictReader "recipe".
# store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(source_file)
# the DictReader method has added some useful information to our data,
# like a `fieldnames` property that lets us access all the values
# in the first or "header" row
print(citibike_reader.fieldnames)

# create a variable to hold the count of each type of Citi Bike user
# assign or "initialize" each with a value of zero (0)

subscriber_count = 0
customer_count = 0 
other_user_count = 0

for a_user in citibike_reader:
    if a_user["usertype"] == 'Subscriber':
        subscriber_count = subscriber_count + 1
    elif a_user["usertype"] == 'Customer':
        customer_count = customer_count + 1
    else:
        other_user_count = other_user_count + 1

print("Number of subscribers:")
print(subscriber_count)
print("Number of customers:")
print(customer_count)
print("Number of 'other' users:")
print(other_user_count)  
