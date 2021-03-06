import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#ignore warnings
import warnings
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def map_varities(species, mapping_dict):
	species = mapping_dict[species]
	return species

def visualize_data(train):
	# print train.describe(include='all')
	sns.barplot(x="SepalLengthCm", y="Species", data=train)
	#graph shows sepallength is a good parameter
	sns.barplot(x="SepalWidthCm", y="Species", data=train)
	# graph shows sepalwidth is a good parameter
	sns.barplot(x="PetalLengthCm", y="Species", data=train)
	# graph shows petallength is a good parameter
	sns.barplot(x="PetalWidthCm", y="Species", data=train)
	# graph shows petalwidth is a good parameter
	# plt.show()

def preprocess_data(dataset):
	Iris_varieties_mapping = {'Iris-setosa' : 0  , 'Iris-versicolor' : 1 , 
	'Iris-virginica' : 2}
	dataset["Species"] = dataset["Species"].apply(map_varities, 
	args = (Iris_varieties_mapping,))
	return dataset

def train_data(dataset):
	y = dataset["Species"]
	X = dataset.drop('Species', axis=1)
	X_train , X_test, y_train , y_test = train_test_split(X, y)
	rcf = RandomForestClassifier().fit(X_train, y_train)
	return rcf, X_train, X_test, y_train, y_test

def calculate_accuracy(predicted, true):
	accuracy = accuracy_score(true, predicted)
	return accuracy

def predict_test(classifier, X_test):
	X_test_predict = classifier.predict(X_test)
	return X_test_predict 		

if __name__ == '__main__':
	dataset = pd.read_csv('Iris.csv')
	visualize_data(dataset)
	dataset = preprocess_data(dataset)
	classifier, X_train, X_test, y_train, y_test = train_data(dataset)
	X_test_predict = predict_test(classifier, X_test)
	test_accuracy = calculate_accuracy(X_test_predict, y_test)
	print test_accuracy