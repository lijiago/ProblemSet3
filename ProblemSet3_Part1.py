#%% Task 1 - Edit code to print as requested #%% treats as code chunk
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = '"Mt. McKinley"' 
elevation = 20322 

print (mountain + ", formerly \nknown as " + nickname + ", \nis " + str(elevation) + "' above sea level.")


#%% Task 2 - Lists and Iteration

data_folder = r'W:\859_data\triangle'

data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

user_item = "roads.shp"

data_list.append(user_item)

for N in data_list: 
    print(data_folder  + "\\" + N)




# %%
