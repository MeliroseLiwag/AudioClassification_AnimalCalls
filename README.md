# Dangerous Animal Detection Through Audio Learning
### Contributors: Katherine Layton, Melirose Liwag

# Report
See the full report and analyses in the file [`FinalReport.pdf`](/FinalReport.pdf)

# Description
This project explores the use of regular Machine Learning techniques (such as Gaussian Mixture Models (GMM) and Support Vector Machines (SVM)) in classifying audio files. As we learned, simple machine-learning techniques could be used on images for a simple classification prompt. Audio files could be simplified into a matrix of values in the same way that images can be simplified into a matrix of pixel values. With this, we decided to experiment with using image classification methods and expanded on said methods for audio classification.

# Data
Data is gathered from the Animal Sound Archive website from a museum in Berlin and contains around 120,000 sound recordings of various species. The downloadable data is available upon request only but the cleaned and final dataset used for this project can be found in [`data.csv`](/Final_Project/data.csv)

The main animal groups we focused on are the Carnivora animal group and the Aves animal group. Further, this project will consider the Aves (birds) group to be safe animals while the Carnivora (Carnivorous animals) group is considered to be dangerous to simplify the classification prompt to be binary.
1. [`CARNIVORA ANIMAL GROUP`](/Final_Project/cleaned_carnivora.csv)
2. [`AVES ANIMAL GROUP`](/Final_Project/cleaned_aves.csv)

One problem with the raw data set that we found was the absence of the animals' actual names in general and thus would be hard for others to understand what animal it was. The scientific names were then found using regular expressions in Python through the provided URL in the raw dataset. The scientific names of the animals were then used to scrub the internet for common names and thus, two additional columns were added to each data frame:
  1. Scientific Name - Contains the Scientific name of each animal within the group.
  2. Common Name - Intuitively, using the common name of the animals within the group would be easily understandable by others.

# Analysis
#### Input Data
Ultimately, the URL columns of each animal group were used to batch-download each '.mp3' file and converted to a '.wav' for easier processing through the Pydub library in Python. Furthermore, only 5 seconds of each audio is kept as we found that it would be the most consistent time signature for all audio files. 

Each audio file is converted to a Mel Spectrogram matrix and Mel Frequency Cepstral Coefficient (MFCC) for use in both SVM and GMM models respectively. An example of a Mel Spectrogram is shown as follows:
![Mel Spectrogram Example](/Final_Project/Images/spectrogram.png)
