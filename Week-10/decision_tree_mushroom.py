## Decision Tree Classifier on Mushroom Dataset from  https://archive.ics.uci.edu/dataset/73/mushroom ##

import pandas as pd
import matplotlib.pyplot as plt

from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# Fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# Data (as pandas dataframes) 
x = mushroom.data.features 
y = mushroom.data.targets 
  
# Change values to numerical
x.replace({'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
           'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
           't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
           '?':0}, inplace=True)


# Show x an y data (uncomment to see)
#print (x.head())
#print(y.head())

# Format settings to show more rows and columns when printing dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Train/test split and decision tree classifier with a 70/30 split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, stratify=y)

clf = DecisionTreeClassifier(random_state=0)
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
plot_tree(clf, feature_names=x.columns, class_names=y['poisonous'].values, filled=True)
plt.tight_layout()
plt.show()





