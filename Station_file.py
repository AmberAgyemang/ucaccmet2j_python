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



# Save as a JSON file

##store as a json file
#with open('dictionairy_names.json', 'w') as file:
    #json.dump(student_dict, file)
