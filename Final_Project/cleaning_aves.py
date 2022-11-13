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

## Take out scientific names with Canau**
drop_rows = []
for row in range(0, data.shape[0]):
    if "Tytalb" in data.iloc[row,-1]:
        drop_rows.append(row)
data.drop(drop_rows, inplace=True)

## Take out "Bru" in scientific names
for row in range(0, data.shape[0]):
    if "Bru" in data.iloc[row, -1]:
        data.iloc[row,-1] = data.iloc[row,-1].replace(" Bru", "")
        
unique = data["Scientific Name"].unique()
print(len(unique)-600)
print("Unique: ", unique[600])

com_names = ["Corn Crake","Iberian Chiffcharr","Great Slaty Woodpecker","Northern Pintail","Marsh Warbler","Ortolan Bunting","Yellowhammer","Cuckoo","Greenfinch","Song Thrush",
             "Blackbird","Garden Warbler","Eurasian Blackcap","Nightingale","European Robin","Eurasian Bittern","Wood Warbler","Willow Warbler","Chiffchaff","Western Bonelli's Warbler",
             "Snipe","Barred Warbler","Eurasian Scops Owl","European Bee-Eater","Bluethroat","Melodious Warbler","Middle Spotted Woodpecker","Quail","Northern Lapwing","Little Crake",
             "Old World Orioles","Redwing","Wood Sandpiper","Hazel Grouse","Northern Hawk-Owl","Tawny Owl","Parasitic Jaeger","Arctic Tern","Whinchat","Eurasian Woodcock",
             "Black-Legged Kittiwake","Water Rail","Spotted Crake","Grey-Headed Chickadee","Willow Tit","Grey Plover","European Golden Plover","Snow Bunting","Black Redstart",
             "Grey Patridge","House Sparrow","Great Tit","Osprey","Eurasian Whimbrel","Western Yellow Wagtail","African Pied Wagtail","Jack Snipe","Thrush Nightingale","Grasshopper Warbler",
             "River Warbler","Broad-Billed Sandpiper","Bar-Tailed Godwit","Black-Tailed Godwit","Gull","Icterine Warbler","Steller's Sea Eagle","Red-Throated Loon","Brambling",
             "Kestrel","Rustic Bunting","Yellow-Breasted Bunting","White-Backed Woodpecker","Whooper Swan","Hooded Crow","Raven","Long-Tailed Duck","Golden Pheasant",
             "Little Ringed Plover","Rosefinch","Redpoll","Temminck's Stint","Lapland Longspur","Purple Sandpiper","Rough-Legged Buzzard","Bohemian Waxwing","Ruddy Turnstone",
             "Red-Throated Pipit","Eurasian Skylark","Sandpiper","Sedge Warbler","Black-Chinned Yuhina","Red-Eyed Vireo","Mistle Thrush","Fieldfare","Ring Ouzel","American Robin",
             "Babbler","Arabian Babbler","Wren","Southern Pied Babbler","Large Grey Babbler","Chestnut-Crowned Laughing Thrush","Sayaca Tanager","Blue-Gray Tanager","Golden Tanager",
             "Paradise Tanager","Masked Tanager","Seven-Colored Tanager","Chestnut-Vented Warbler","Long-Billed Crombec","Sardinian Warbler","Dartford Warbler","Lesser Whitethroat",
             "Spectacled Warbler","Whitethroat","Eastern Subalpine Warbler","Starling","White-Shouldered Starling","Chestnut-Tailed Starling","White-Headed Starling","White-Necked Myna",
             "Brahminy Starling","Vinous-Throated Parrotbill","Saffron Finch","Grossbeak Starling","White-Capped Tanager","European Stonechat","Streaked Scrub Warbler","Golden-Billed Saltator",
             "Coleto","Chaco Sparrow","Sand Martin","Brown-Throated Martin","Goldcrest","Brazilian Tangaer","Firecrest","Eurasian Crag Martin","Rock Martin","Groundscrapper Thrush",
             "Grey-Headed Parrotbill","Gray-Rumped Swallow","Grey-Breasted Martin","Graceful Prinia","Plain Prinia","Black-and-Rufous Warbling Finch","Rusty-Cheeked Scimitar Babbler",
             "Masked Gnatcatcher","White-Necked Rockfowl","Grey-Necked Rockfowl","Redstart","Yellow Grosbeak","Ring-Necked Pheasant","Coal Tit","Streal-Throated Swallow","Rosy Starling",
             "Blue Grosbeak","Orange-Breasted Bunting","Red-Cowled Cardinal","Grey Tit","Yellow-Billed Cardinal","Red-Crested Cardinal","Bearded Reedling","Bristle-Crowned Starling",
             "Blackstart","Tristam's Starling","Mourning Wheatear","Capped Wheatear","Variable Wheatear","White-Crowned Wheatear","Western Black-Eared Wheatear","Northern Wheatear",
             "Sooty Chat","Spotted Flycatcher","Blue Whistling Thrush","Blue Rock Thrush","Golden Myna","Brown-Capped Whitestart","Yellow-Faced Myna","Chalk-Browed Mockingbird","Blue-Winged Minla",
             "Superb Fairywren","Crested Tit","Savi's Warbler","Black-Crested Finch","Bali Myna","Silver-Eared Mesia","Red-Billed Leiothrix","Ashy Starling","Superb Starling","Golden-Breasted Starling",
             "Cape Starling","Long-Tailed Glossy Starling","Emerald Starling","Greater Blue-Eared Starling","Bronze-Tailed Starling","Splendid Starling","Golden-Collared HoneyCreeper",
             "Olivaceous Warbler","Barn Swallow","Wire-Tailed Swallow","White-Eared SIbia","Yellow Cardinal","Common Hill Myna","Black-Collared Starling","Indian Pied Myna",
             "Masked Yellowthroat","Orange-Headed Thrush","Greater Necklaced Laughing Thrush","White-Crested Laughing Thrush","Rufous-Chinned Laughing Thrush","White-Throated Laughing Thrush",
             "Lesser Neckladed Laughing Thrush","Red-Breasted Flycatcher","Collared Flycatcher","European Pied Flycatcher","White-Vented Euphonia","Violaceous Euphonia","Karoo Scrub Robin",
             "Burnt-Neck Eremomela","Cinnamon-Breasted Bunting","Reed Bunting","Black-Headed Bunting","Crested Bunting","Golden-Breasted Bunting","Corn Bunting","Cirl Bunting","Red-Headed Bunting",
             "Dicua Finch","House Martin","Blue Dacnis","Eurasian Blue Tit","Red-Legged Honeycreeper","Black=Throated Canary","Wattled Starling","White-Browned Robin-Chat","Red Pileated FInch",
             "White-Rumped Shama","Magpie Tanager","Rattling Cisticola","White-Throated Dipper","Violet-Backed Starling","Zitting Cisticola","Spotted Palm Thrush","Black-and-Yellow Tanager",
             "Cetti's Warbler","Red-Rumped Swallow","Greater Striped Swallow","Northern Cardinal","Hooded Mountain Tanager","Yellow-Billed Oxpecker","Red-Billed Oxpecker","Marico Flycatcher",
             "Sulawesi Myna","Apo Myna","Striated Starling","Singing Starling","Scarlet-Headed Blackbird","Golden-Crested Myna","Yellow-Winged Blackbird","Tawny-Shouldered Blackbird","Long-Tailed Tit",
             "Eurasian Reed Warbler","Great Reed Warbler","Moustached Warbler","Bank Myna","Myna","Lesser Swamp Warbler","African Reed Warbler","Vinous-Breasted Starling","Black-Winged Starling",
             "Olive Oropendola","Montezuma Oropendola","Brown-and-Yellow Marshbird","Chestnut-Headed Oropendola","Green Oropendola","Crested Oropendola","Caped Wagtail","White Wagtail","Grey Wagtail",
             "Epaulet Oriole","Tree Pipit","Meadow Pipit","Long-Billed Pipit","Yellowish Pipit","Australian Pipit","Berthelot's Pipit","Desert Lark","Grayish Baywing","Indian White-Eye","Shaft-Tailed Whydah",
             "Pin-Tailed Whydah","Long-Tailed Paradise Whydah","Straw-Tailed Whydah","Whydah","Violet-Eared Waxbill","Red-Cheeked Cordon-Bleu","African Paradise Flycatcher","Australian Zebra Finch",
             "Double-Barred Finch","Scaly-Feathered Weaver","Western Bluebill","Diamond Firetail","European Serin","Syrian Serin","Atlantic Canary","Eurasian Nuthatch","Desert Finch","Eurasian Penduline Tit",
             "Red-Billed Quelea","Red-Whiskered Bulbul","Eurasian Bullfinch","African Red-Eyed Bulbul","White-Spectacled Bulbul","Black-Headed Bulbul","White-Eared Bulbul","Red-Vented Bulbul","Dunnock",
             "Alpine Accentor","Southern Masked Weaver","Village Weaver","Vitelline Masked Weaver","White-Browed Sparrow-Weaver","Chestnut Weaver","Buru Friarbird","Eurasian Tree Sparrow","Dead Sea Sparrow",
             "Great Sparrow","Cape Sparrow","Spanish Sparrow","Helmeted Friarbird","Arabian Golden Sparrow","Sociable Weaver","African Quailfinch","Star Finch","Crimson Finch","Bronzy Sunbird","Cardinal Myzomela",
             "Cape Clapper Lark","White-Winged Grosbeak","Belford's Melidectes","Calandra Lark","Green-Backed Twinspot","Woodlark","Red Crossbill","Java Sparrow","Scaly-Breasted Munia","White-Rumped Munia","Bronze Mannikin",
             "Tricoloured Munia","Red-Billed Firefinch","ASian Fairy-Bluebird","Red-Throated Twinspot","Yellow-Throated Sparrow","Crested Lark","Thekla's Lark","Tenerife blue Chaffinch","Chaffinch",
             "Black-Rumped Waxbill","Yellow-Mantled Widowbird","Oranged-Cheeked Waxbill","Gouldian Finch","Long-Tailed Widowbird","Lavender Waxbill","African Silverbill","Southern Red Bishop","Black-Headed Waxbill",
             "Indian Silverbill","Pin-Tailed Parrotfinch","Black-Faced Waxbill","Grey-Backed Sparrow-Lark","Jackson's Widowbird","Waxbill","Chestnut-Backed Sparrow-Lark","Fork-Tailed Drongo","Greater Racket-Tailed Drongo",
             "Yellow Canary","Yellow-Fronted Canary","Hawfinch","Palestine Sunbird","Dusky Sunbird","Northern Double-Collared Sunbird","Variable Sunbird","Shining Sunbird","Spiked-Heeled Lark","Cape Long-Billed Lark",
             "Twite","Sinai Rosefinch","European Goldfinch","Pale Rockfinch","Linnet","Citril Finch","Red Siskin","Sabota Lark","Red-Capped Lark","Greater Short-Toed Lark","Mediterranean Short-Toed Lark",
             "Trumpeter Finch","Pirit Batis","Cape Penduline Tit","Red Avadavat","Red-Headed Finch","Orange-Breasted Waxbill","Cut-Throat Finch","Fork-Tailed Sunbird","Andean Condor","Blood-Colored Woodpecker",
             "Magpie Shrike","Blue-Naped Mousebird","Red-Billed Blue Magpie","Eurasian Hoopoe","African Grey Hornbill","Von der Decken's Hornbill","Cabot's Tragopan","Black-Headed Ibis","Satyr Tragopan","Bateleur",
             "Temminck's Tragopan","Crowned Hornbill","African Sacred Ibis","Blyth's Tragopan","Straw-Necked Ibis","Northern Red-Billed Hornbill","Buff-Necked Ibis","Crested Barbet","Fork-Tailed Woodnymph",
             "Purple-Crested Turaco","White-Backed Duck","Livingstone's Turaco","Knysna Turaco","Hartlaub's Turaco","Sacred Kingfisher","White-Cheeked Turaco","Western Capercaillie","Australian Shelduck",
             "White-Crested Turaco","Striped Cuckoo","Himalayan Snowcock","Paradise Shelduck","Shelduck","Radjah Shelduck","Yellow-Billed Turaco","Collared Brush-Turkey","Black-Billed Turaco","Ruddy Shelduck",
             "Chaco Eathcreeper","Falkland Steamer Duck","South African Shelduck","Reeves's Pheasant","Mikado Pheasant","Elliot's Pheasant","Mrs. Hume's Pheasant","Sooty-Fronted Spinetail","Crested Serpent Eagle",
             "Crowned Eagle","Bronze-Winged Duck","Ornate Hawk-Owl","Black-and-White Hawk-Eagle","Eider","Spot-Billed Toucanet","Twelve-Wired Bird-of-Paradise","Sooty Tyrannulet","Toucan Barbet","Hamerkop","King Vulture",
             "Secretarybird","Andean Cock-of-the-Rock","Blyth's Hornbill","Wreathed Hornbill","Crested Partridge","Scimitarbill","Toco Toucan","Channel-Billed Toucan","Green-Billed Toucan","Keel-Billed Toucan",
             "Yellow-Throated Toucan","White-Throated Toucan","Red-Billed Chough","Alpine Chough","Koklass Pheasant","Satin Bowerbird","Piapiac","Lettered Aracari","Firey-Billed Aracari","Black-Necked Aracari",
             "Red-Billed Spurfowl","Red-Naped Ibis","Fire-Tufted Barbet","Brown Cacholote","Bare-Throated Bellbird","Three-Wattled Bellbird","White Bellbird","Grey Peacock-Pheasant","Bronze-Tailed Peacock-Pheasant",
             "Palawan Peacock-Pheasant","African Harrier-Hawk","Martial Eagle","Germain's Peacock-Pheasant","Glossy Ibis","Spur-Winged Goose","Puna Ibis","Red-Cheeked Wattle-Eye","Crested Jayshire","Indian Pitta",
             "Blue-Throated Piping Guan","European Green Woodpecker","Magpie","Black-Headed Woodpecker","Arrowhead Piculet","Grey-Heades Woodpecker","White-Tipped Plantcutter","Chilean Flamingo","Greater Falmingo",
             "White-Hooded Wood Hoopoe","Green Wood Hoopoe","American Flamingo","James's Flamingo","Andean Flamingo","Small Minivet","Lesser Flamingo","Jungle Bush Quail","Little Thornbird","European Honey Buzzard",
             "Resplendent Quetzal","Crested Guan","Visayan Hornbill","Indian Peafowl","Horned Curassow","Green Peafowl","Stork-Billed Kingfisher","Dusky-Legged Guan","Raggiana Bird-of-Paradise","Greater Bird-of-Paradise",
             "Red Bird-of-Paradise","Lesser Bird-of-Paradise","Harris's Hawk","Ruddy Duck","Litle Chachalaca","Chaco Chachalaca","Mountain Quail","Indian Grey Hornbill","Caatinga Puffbird","Spotted NutCracker",
             "Black-Crowned Night Heron","Helmeted Guineafowl","Orinoco Goose","Ross's Turaco","Black Kite","Alagaos Curassow","Salvin's Curassow","Yellow-Fronted Woodpecker","Ocellated Turkey","Swallow-Tailed Bee-Eater",
             "Red Kite","Green Ibis","Black Bee-Eater","Little Bee-Eater","White Woodpecker","Turkey","Black-Cheeked Woodpecker","Yellow-Billed Stork","Cattle Tyrant","Yellow-Tufted Woodpecker","blue-Breasted Bee-Eater",
             "West Indian Woodpecker","Maleo","Pale Chanting Goshawk","Ringed Kingfisher","Brown-Headed Barbet","Blue-Cheeked Bee-Eater","Great Barbet","Asian Green Bee-Eater","Grey-Headed Bushshrike","Black Grouse",
             "Double-Toothed Barbet","Black-Collared Barbet","Crested Fireback","Edwards's Pheasant","Great Grey Shrike","Red-Backed Shrike","Silver Pheasant","Crimson-Breasted Shrike","Lesser Grey Shrike","Himalayan Monal",
             "Hooded Merganser","Siamese Fireback","Crestless Fireback","White-Tailed Shrike","Marabou Stork","Tufted Tit-Spinetail","Swinhoe's Pheasant","Willow Ptarmigan","Narrow-Billed Woodcreeper","Long-Crested Eagle",
             "Bulwer's Pheasant","Crested Duck","Greater Adjutant","Grey-Backed Fiscal","Papyrus Gonolek","Long-Tailed Shrike","Yellow-Crowned Gonolek", "Southern Fiscal"]
print("Common Names:", len(com_names))

## Create a dictionary to map the scientific names tot he common names
sci_to_com = {}
for i in range(0,len(com_names)):
    sci_to_com[unique[i]] = com_names[i]

## Add the Common Names column to the original data frame
sci_name_list = []
dict_keys = unique[0:601]
for row in range(0, data.shape[0]):
    if data.iloc[row,-1] in dict_keys:
        sci_name_list.append(sci_to_com[data.iloc[row,-1]])
    else:
        sci_name_list.append(None)
data["Common Name"] = sci_name_list
data.dropna(inplace=True)
data.to_csv("[WIP]cleaned_aves.csv", index=False)
'''
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
'''
