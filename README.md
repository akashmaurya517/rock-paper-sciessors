# rock-paper-sciessors
### Here’s the list of all dependencies that we need to take of before running the game. 
1.	Numpy
2.	OpenCV
3.	Keras
4.	TensorFlow 
5.	Sklearn
6.	Matplotlib

## APPROACH, TECHNIQUES AND ALGORITHMS
We have taken the following approach to do the project.
1. Data collection
  a. Training data
  b. Testing data
2. Preprocessing the data
3. Training the model through data
4. Using the trained model to play the game.


## Data Collection
Data collection is a very useful aspect of any data-driven project. though the deep learning model needs a huge amount of data. we created our own. it has two benefits. we don’t need to bother about searching the data we can directly create one. and secondly the model will be fitted on your own hand image, so it tends to make more accurate predictions while playing the game. 

In our notebook code, we have to rerun a couple of cells multiple times to generate the data set for every possible combination of training, testing, and Rock, paper, scissor class. Thus we generated six combinations such as training data for rock class, training data for paper class, training data for scissors class. As well as testing data for Rock class, testing data for paper class and testing data for scissors class. Every training data has one thousand and one sample for each class Rock paper and scissors. And every testing data has 101 samples for each Rock paper and scissor class.

                    
To generate the whole data set you have to run the previous cell for every combination of class_type and class_num parameter. and then run the next cell. running the next cell will automatically generate the defined number of data set for the corresponding combination. 
it will generate 1001 (0 to 1000) data samples for every class in training data and 101(0 to 100) data samples for every class for validation/ testing data.
while running the next cell you have to make a hand gesture of the corresponding data set that you are generating in front of the camera. the code will open the camera and take the snapshot of the hand process it and then save it into the directory. for example while the value of the given parameters class_type and class_num are “valid” and “1” respectively. then it will generate 101 testing data sample images for the paper class.

### I have encoded the class labels for both training and testing data as below
class Rock → 0

class paper→ 1

class scissors → 2

## How to use.
1. Run the notebook code generat the data and make the model.(make sure the directories are made)
2. run play_game.py to play the game
 
