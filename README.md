# Dangerous Animal Detection Through Audio Learning
### Contributors: Katherine Layton, Melirose Liwag

# Report
See the full report and analyses in the file [`FinalReport.pdf`](/FinalReport.pdf)

# Description
This project explores the use of regular Machine Learning techniques (such as Gaussian Mixture Models (GMM) and Support Vector Machines (SVM)) in classifying audio files. As we learned, simple machine-learning techniques could be used on images for a simple classification prompt. Audio files could be simplified into a matrix of values in the same way that images can be simplified into a matrix of pixel values. With this, we decided to experiment with using image classification methods and expanded on said methods for audio classification.

# Novelty
1. Attempts classification on audio files
2. Custom dataset, consisting of 2 datasets curated for this project
3. Use of simple modeling techniques in lieu of state-of-the-art audio classification methods
   
# Data
Data is gathered from the Animal Sound Archive website from a museum in Berlin and contains around 120,000 sound recordings of various species. The downloadable data is available upon request only but the cleaned and final dataset used for this project can be found in [`data.csv`](/Final_Project/Data/data.csv)

The main animal groups we focused on are the Carnivora animal group and the Aves animal group. Further, this project will consider the Aves (birds) group to be safe animals while the Carnivora (Carnivorous animals) group is considered to be dangerous to simplify the classification prompt to be binary.
1. [`CARNIVORA ANIMAL GROUP`](/Final_Project/Data/cleaned_carnivora.csv)
2. [`AVES ANIMAL GROUP`](/Final_Project/Data/cleaned_aves.csv)


See more info about data pre-processing in the following files:
  1. [`Canivora DataSet`](/Final_Project/Code/cleaning_carnivora.py)
  2. [`Aves DataSet`](/Final_Project/Code/cleaning_aves.py)

# Exploratory Data Analysis
See full EDA n [`EDA.ipynb`](/Final_Project/Notebooks/EDA.ipynb)

One problem with the raw data set that we found was the absence of the animals' actual names in general and thus would be hard for others to understand what animal it was. The scientific names were then found using regular expressions in Python through the provided URL in the raw dataset. The scientific names of the animals were then used to scrub the internet for common names and thus, two additional columns were added to each data frame:
  1. Scientific Name - Contains the Scientific name of each animal within the group.
  2. Common Name - Intuitively, using the common name of the animals within the group would be easily understandable by others.

# Analysis
### Steps:
  1. Data Mining - Curating data specific to this project
  2. Data pre-processing - Convert data into '.wav' files for easier classification through Python
  3. Dimensionality Reduction - Using Principal Component Analysis (PCA) to reduce the dimensions of spectrograms for a simpler model
  4. Model Building - GMM and SVM used to classify audio files

#### Input Data
Ultimately, the URL columns of each animal group were used to batch-download each '.mp3' file and converted to a '.wav' for easier processing through the Pydub library in Python. Furthermore, only 5 seconds of each audio is kept as we found that it would be the most consistent time signature for all audio files. 

Each audio file is converted to a Mel Spectrogram matrix and Mel Frequency Cepstral Coefficient (MFCC) for use in both SVM and GMM models respectively. An example of a Mel Spectrogram is shown as follows:

#### Mel Spectrogram:
![Mel Spectrogram Example](/Final_Project/Images/spectrogram.png)

#### MFCC: 
![MFCC Example](/Final_Project/Images/MFCC.PNG)

More info on creating the spectrograms can be viewed in [`CreateSpectro.ipynb`](/Final_Project/Notebooks/CreateSpectro.ipynb) right here on GitHub. 

### Model Evaluation 
Due to the large number of features found in both the MFCC and Mel spectrograms, we used PCA to extract only the features necessary to explain the data as a whole. A train/test split of 90-10 is used to train and test our models to aim for the higher possible accuracy. It is important to keep in mind that the resulting data set is made up of a random sampling of (about) equal parts Carnivora and Aves.

#### Models - GMM
GMM was only able to classify the audio files by 69% with PCA tuned with 95% variability.
  - correctly classifies 72% as not dangerous (birds) and 66% as dangerous (carnivorous animals)
  - More data is needed to establish the reliability and viability of the model
Accuracies are pretty low to our taste but it is the best we could do with GMM after different parameter testings.

![GMM Summary](/Final_Project/Images/GMM_summary.PNG)

#### Models - SVM
A base SVM model was tuned with 4 PCA components instead of the 95% variability PCA parameter used for GMM. Labels of each animal group were also changed to a binary component to perform One-Class SVM. 
  - SVM performed better with lower dimensions than GMM
  - base accuracy of 59.09% with MFCC as input data and a base accuracy of 58.29% with Mel spectrogram as input data
We decided to test our SVM model with varying gamma values while using the RBF kernel in hopes of improving our model.
  - gamma value of 9.800000000000001e-06 gave us the best accuracy of 91.98% with MFCC as input data
  - gamma value of 9.9e-06 gave us the best accuracy of 93.32% with Mel spectrogram as input data

![SVM accuracy vs. Gamma (MelSPectro)](/Final_Project/Images/SVM_MelSpectro.PNG)
![SVM accuracy vs. Gamma (MFCC)](/Final_Project/Images/SVM_MFCC.PNG)
