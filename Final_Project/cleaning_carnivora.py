### Computational Data Analytics - ISYE 6740
## GaTech Fall Semester 2022
## By: Melirose Liwag, Katherine Layton
## gtID: 903733651, 
#####
#### RUN ONLY WHEN CLEANED_CARNIVORA.CSV IS NOT YET CREATED ####
### Final Project
##  cleaning_carnivora.py
##  - Code for cleaning up strings and adding a common name to the
##    original data set.
##  - Change column names to be more intuitive
##  - To be joined with the bird data set
#####
import pandas as pd
import re

## Get Carnivora Data
data = pd.read_csv("Carnivora\multimedia.txt", delim_whitespace=True)

## Rename URL column (more intuitive)
data.rename(columns={"identifier": "URL"}, inplace=True)

## Create new column for animal labels
data["group"] = ["Carnivora"]*data.shape[0]
data["Common Name"] = [""]*data.shape[0]
sci_names = []

## Clean up Scientific Name of each animal
for row in range(0, data.shape[0]):
    raw = re.search(
        "(?<=http://www.tierstimmenarchiv.de/recordings/)\w+",
        data.iloc[row,3])
    raw = raw.group(0)
    sci_name = re.search(
        "\w+(?=_[A-Z]*[\w]*_[\w]*[_\w*]*_short)",
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

## Take out scientific names with Canau**
drop_rows = []
for row in range(0, data.shape[0]):
    if "Canau" in data.iloc[row,-1]:
        drop_rows.append(row)

data.drop(drop_rows, inplace=True)
    
unique = data["Scientific Name"].unique()

com_names = ["African Lion","European Polecat","African Golden Wolf","Cross Fox","Beech Marten","Common Seal","Domestic Dog","Domestic Dog","Giant Panda","Tiger",
             "Eurasian Lynx","California Sea Lion","Snow Leopard","Clouded Leopard","European Pine Marten","Canada Lynx","Common Otter","Domestic Cat","Maned Wolf",
             "Arctic Wolf","Cheetah","Fenec Fox","Ruppell's Fox","Ruppell's Fox","Arctic Fox","Corsac Fox","Arctic Fox","Asian Black Bear","Polar Bear","Brown Bear",
             "Gray Fox","Spectacled Bear","Meerkat","Bush Dog","Baikal Seal","Ringed Seal","Cougar","Jaguarundi","Giant Otter","Raccoon","Crab-Eating Raccoon","Fishing Cat",
             "Kinkajou","Asian Palm Civet","Tiger","Tiger","Leopard","Jaguar","Lion","South American Sea Lion","South American Sea Lion","Walrus","Common Raccoon Dog",
             "South American Coati","White-Nosed Coati","Siberian Weasel","Weasel","Narrow-Striped Mongoose","Banded Mongoose","Banded Mongoose","Southern Elephant Seal",
             "Northern Elephant Seal","Sloth Bear","Yellow-Throated Marten","Bobcat","African Wild Dog","Serval","Ocelot","Brown Hyena","Striped Hyena","Common Dwarf Mongoose",
             "Sun Bear","Grey Seal","Wolverine","Broad-Striped Malagasy Mongoose","Ring-Tailed Vontsira","Domestic Cat","European Wildcat","Jungle Cat","Steller Sea Lion",
             "Sea Otter","Yellow Mongoose","Dhole","Crocuta","Asian Golden Cat","Caracal","New Guinea Singing Dog","Domestic Dog","Dingo","Coyote","Golden Jackal",
             "Northern Fur Seal","Brown Fur Seal","South American Fur Seal","Binturong","Asian Small-Clawed Otter","Red Panda"]

## Create a dictionary to map the scientific names to the common names
sci_to_com = {}
for i in range(0, len(unique)):
    sci_to_com[unique[i]] = com_names[i]

## Add the Common Names column to the original data frame
sci_name_list = []
for row in range(0, data.shape[0]):
    sci_name_list.append(sci_to_com[data.iloc[row,-1]])
data["Common Name"] = sci_name_list

data.to_csv("cleaned_carnivora.csv", index=False)
