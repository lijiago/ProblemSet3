#%% Task 1 - Edit code to print as requested #%% treats as code chunk
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = '"Mt. McKinley"' 
elevation = 20322 

print (mountain + ", formerly \nknown as " + nickname + " \nis " + str(elevation) + "' above sea level.")


#%% Task 2 - Lists and Iteration

data_folder = r'W:\859_data\triangle'

data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

user_item = "roads.shp"

data_list.append(user_item)

for N in data_list: 
    print(data_folder  + "\\" + N)

# %% Task 3 - Lists and Iteration

user_numbers = []

for i in range(3):
    user_input=int(input("Enter an integer:"))
    user_numbers.append(user_input)
    user_numbers.sort()
print(user_numbers[-1])

# %% Task 3 - Challenge

user_numbers = []

for i in range(3):
    user_input=int(input("Enter an integer:"))
    user_numbers.append(user_input)
    user_numbers.sort(reverse=True)
print(user_numbers)

 

#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")


#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)


#%% Task 4.3

#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
    
#Split the data into values
    lineData=lineString.split(",")
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[0]
#Extract the fleet value
    fleet = lineData[4]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
    

#%% Task 4.4

vesselID = "258799000"
vesselCountry = vesselDict[vesselID]

print("Vessel #" + str(vesselID) + " flies the flag of " + vesselCountry)


#%%Task 5 
#Create a Python file object, i.e., a link to the file's contents
fileObj2 = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList2 = fileObj2.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj2.close() #Close the file

#checking index values
headerLineString2 = lineList2[0]
headerItems2 = headerLineString2.split(",")

mmsi_idx = headerItems2.index('transshipment_mmsi')
startlat_idx = headerItems2.index('starting_latitude')
startlong_idx = headerItems2.index('starting_longitude')
endlat_idx = headerItems2.index('ending_latitude')
endlong_idx = headerItems2.index('ending_longitude')

print(mmsi_idx,startlat_idx, startlong_idx, endlat_idx, endlong_idx)

#Iterate through all lines (except the header) in the data file:
for lineString2 in lineList2[1:]:

    #Split the data into values
    lineData2=lineString2.split(",")

    #storing values as variables
    mmsi = (lineData2[0])
    startlat = float(lineData2[1])
    startlong = float(lineData2[2])
    endlat = float(lineData2[3])
    endlong = float(lineData2[4])

    #check if the event crosses the equator; and check if starting longitude falls between 165 and 170E
    
    if startlat < 0 and endlat > 0 and 165<startlong<170: 
    # using the value of the transshipment_mmsi to query the vesselsDict created above to print the vessel’s mmsi and its fleet.
         print("Vessel #" + str(mmsi) + " flies the flag of " + str(vesselDict[mmsi]))   
    #else: 
       # print("No vessels met criteria")
    #else startlat < 0 and endlat > 0 and 165<startlong<170:
       # print("No vessels met criteria")
 

        
       


