### Computational Data Analytics - ISYE 6740
## GaTech Fall Semester 2022
## By: Melirose Liwag, Katherine Layton
## gtID: 903733651, 
#####
#### RUN ONLY WHEN CLEANED_AVES.CSV IS NOT YET CREATED ####
### Final Project
##  cleaning_aves.py
##  - Code for cleaning up strings and adding a common name to the
##    original data set.
##  - Change column names to be more intuitive
##  - To be joined with the carnivora data set
#####
import pandas as pd
import re

## Get Aves Data
data = pd.read_csv("Aves\multimedia.txt", delim_whitespace=True)

## Rename URL column (more intuitive)
data.rename(columns={"identifier": "URL"}, inplace=True)

## Create new column for animal labels
data["group"] = ["Aves"]*data.shape[0]
data["Common Name"] = [""]*data.shape[0]
sci_names = []

## Clean up Scientific Name of each animal
for row in range(0, data.shape[0]):
    raw = re.search(
        "(?<=http://www.tierstimmenarchiv.de/recordings/)\w+",
        data.iloc[row,3])
    raw = raw.group(0)
    sci_name = re.search(
        "\w+(?=_[\w]*[\w]*_[\w]*[_\w*]*_short)",
        raw)
    if sci_name == None:
        sci_name = re.search(
            "\w+(?=_short)",
            raw)
    sci_name = sci_name.group(0)
    sci_name = sci_name.replace("_", " ")
    sci_names.append(sci_name)

data["Scientific Name"] = sci_names

## What Columns are we dealing with
cols = data.columns

## Take out scientific names with Tytalb**
drop_rows = []
for row in range(0, data.shape[0]):
    if "Tytalb" in data.iloc[row,-1]:
        drop_rows.append(row)
data.drop(drop_rows, inplace=True)

## Take out "Bru" and "Tre" and " Thi Certhia 60" in scientific names
for row in range(0, data.shape[0]):
    if "Bru" in data.iloc[row, -1]:
        data.iloc[row,-1] = data.iloc[row,-1].replace(" Bru", "")
    if "Tre" in data.iloc[row, -1]:
        data.iloc[row,-1] = data.iloc[row,-1].replace(" Tre", "")
    if "Thi Certhia 60" in data.iloc[row, -1]:
        data.iloc[row,-1] = data.iloc[row,-1].replace(" Thi Certhia 60", "")
    ## Further clean up bird names
    if "Phylloscopus trochilus" in data.iloc[row, -1]:
        data.iloc[row,-1] = data.iloc[row,-1].replace(data.iloc[row,-1]
            , "Phylloscopus trochilus")
        
unique = data["Scientific Name"].unique()
#print("Unique: ", unique[1300:1400])
file = open("Aves_commonNames.txt","r+")
lines = file.readlines()
com_names = []
for line in lines:
    com_names = com_names + list(filter(None,line.strip('\n').split(",")))
file.close()
print("Left: ",len(unique)-len(com_names))
print("Done: ",len(com_names))

## Create a dictionary to map the scientific names to the common names
sci_to_com = {}
for i in range(0,len(com_names)):
    sci_to_com[unique[i]] = com_names[i]

## Add the Common Names column to the original data frame
sci_name_list = []
dict_keys = unique[0:len(com_names)]
for row in range(0, data.shape[0]):
    if data.iloc[row,-1] in dict_keys:
        sci_name_list.append(sci_to_com[data.iloc[row,-1]])
    else:
        sci_name_list.append(None)
clean = data.copy()
clean["Common Name"] = sci_name_list
clean.dropna(inplace=True)
print("Total Data Points: ", clean.shape[0], "/", data.shape[0],
      ",", round((clean.shape[0]/data.shape[0])*100,2), "% Complete" )
clean.to_csv("cleaned_aves.csv", index=False)

