## Decision Tree Classifier on Car Evaluation Dataset from  https://archive.ics.uci.edu/dataset/19/car+evaluation ##

import pandas as pd
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# Fetch dataset 
car_evaluation = fetch_ucirepo(id=19) 
  
# Data (as pandas dataframes) 
x = car_evaluation.data.features 
y = car_evaluation.data.targets 

# Change values to numerical
x.replace({'vhigh':4, 'high':3, 'med':2, 'low':1, 
           '5more': 5, 'more': 5, 
           'small': 1, 'medium': 2, 'big': 3}, inplace=True)

# Show x an y data (uncomment to see)
#print (x.head())
#print(y.head())

# Format settings to show more rows and columns when printing dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Train/test split and decision tree classifier with a 70/30 split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, stratify=y)

# Create Decision Tree with a speified depth
clf = DecisionTreeClassifier(max_depth= 6, random_state=0)
#clf = DecisionTreeClassifier(random_state=0) # no depth specified
clf.fit(x_train, y_train)

# Evaluate on test set
preds = clf.predict(x_test)
print ("test accuracy:", accuracy_score(y_test, preds)) # Print test accuracy

# Define cross-validation
kf = KFold(n_splits = 9, shuffle = True, random_state = 0)

# Cross-validate
cv_scores =  cross_val_score(clf, x, y, cv=kf)

print (cv_scores)

# Plot tree graphically
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=x.columns, class_names=y['class'].values, filled=True)
plt.tight_layout()
#plt.show()





