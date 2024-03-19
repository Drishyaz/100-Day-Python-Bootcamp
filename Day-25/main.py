# with open("./weather_data.csv") as f:
#     data = f.readlines()
#
# print(data)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print(len(data))
#     for d in data:
#         if d[1] != 'temp':
#             temperatures.append(int(d[1]))
#
#     print(temperatures)

# PANDAS IS A DATA ANALYSIS LIBRARY
import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])                     # to print a specific column -> series

# data_dict = data.to_dict()              # to convert a pandas object to a dict
# print(data_dict)
#
# temp_list = data["temp"].to_list()      # to convert a series/column to a list
# print(temp_list)
#
# print(data["temp"].mean())              # to find the average of a series
# print(data["temp"].max())               # to find the maximum of a series
#
# print(data["condition"])                # Get Data in Columns
# # print(data.condition)
#
# print(data[data.day == "Monday"])              # Get Data in Rows
# print(data[data.temp == data.temp.max()])      # print the row with maximum temperature

# monday = data[data.day == "Monday"]            # Fetch temperature of Monday
# print(monday.condition)                        # Convert Celsius to Fahrenheit
# print(f"{monday.temp[0]} C")
# fahrenheit = ((monday.temp[0]) * 9/5) + 32
# print(f"{fahrenheit} F")

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Diya", "Avik", "Gopal"],
#     "scores":   [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)              # Converting dict to to dataframe
# print(data)
# data.to_csv("new_data.csv")                     # Converting dataframe to csv

# We will analyse and extract data from this CSV file and create a new CSV file from it
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240319.csv")  # read the csv file
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])                     # count the gray squirrels
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])                  # count the red squirrels
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])                   # count the black squirrels

data_dict = {                                                                   # create a dict of color, count
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)                                                # convert this data to a dataframe
df.to_csv("squirrel_count.csv")                                                 # convert the dataframe to a CSV

