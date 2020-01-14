

# PART I

# Look into the csv file for the Seatle station
#Seattle,WA,GHCND:US1WAKG0038

#import json
import json

# Load in json file
with open('precipitation.json', encoding='utf8') as file:
    data = json.load(file)

# Save the station code of Seatle in a variable
Seatle_station_code = 'GHCND:US1WAKG0038'

#Create a new list to save data in 

json_list = []

#create a list fileed with the correct dictionairies, containing the measurements of the Seatle staates
for measurement in data:
    # check if code of dictionairy corresponds with seatle code
    #if true add the selected dictionairy to json_dict
    if measurement['station'] == Seatle_station_code:
        json_list.append(measurement)

    
print(json_list)
        
# Sum all the measurements of the location of Seatle for each month: create a list with the toal monthly precipation

#create a list with 12 zeros: representing 12 empty buckets
month_list = [0]*12

#create a for loop to take action for each measurement
for dic in json_list:
    #select the month from the date
    date = dic ['date']
    correct = date.split ('-')
    month = correct [1]
 
    # sum all values of each month, 
    month_list[int(month)-1] += dic['value']
    
#print the result
print(month_list)


#Save as a JSON file
with open('exercise1.json', 'w', encoding='utf8') as file:
    json.dump(month_list, file)


#PART II: 

# Calculating the sum of the whole year
value_whole_year = sum(month_list)
print(f'The precipation of Seatle of the whole year is {value_whole_year}')

# Calculating the relative precipation per unt


#  creating empty list to add the relative values per month
rel_list = []

for month_value in month_list:
# to calculate the relative precipitation 
    rel_list.append(month_value*100/value_whole_year)

#print result
print(rel_list)


#Store result in jason file
with open('relative_precipitation.json', 'w', encoding='utf8') as file:
    json.dump(rel_list, file)
