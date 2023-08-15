### Computational Data Analytics - ISYE 6740
## GaTech Fall Semester 2022
## By: Melirose Liwag, Katherine Layton
## gtID: 903733651, 
#####
#### RUN ONLY WHEN DATA.CSV IS NOT YET CREATED ####
### Final Project
##  joining_datasets.py
##  - Code for joining the Aves and Carnivora data sets to build the final
##    dataset for the Project
#####
import pandas as pd

### Data set without labels ###
## Get Aves dataset
aves = pd.read_csv("cleaned_aves.csv")

## Get Carnivora dataset
carnivora = pd.read_csv("cleaned_carnivora.csv")

## Join both data sets and save the final dataset
data = pd.concat([aves,carnivora])
data.to_csv("data_nolabel.csv", index=False)

### Data set with labels ###
aves_label = aves.copy()
aves_label["Type"] = ["Not Dangerous"]*aves_label.shape[0]

carnivora_label = carnivora.copy()
carnivora_label["Type"] = ["Dangerous"]*carnivora_label.shape[0]

## Join both data sets and save the final dataset
data_label = pd.concat([aves_label, carnivora_label])
data_label.to_csv("data.csv", index=False)
