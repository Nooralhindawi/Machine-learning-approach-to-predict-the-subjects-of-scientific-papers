# -*- coding: utf-8 -*-
"""Assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1euDropjBwY42rT98GRIKhN83inEss6C3
"""

#Moutend to my drive, can be mounted easily in any drive (I shared the link to anyone)
from google.colab import drive
drive.mount("/content/gdrive")

"""# Importing libraries"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import f1_score
import numpy as np
from sklearn.model_selection import KFold
# %matplotlib inline
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from statistics import mean, stdev
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import re
from sklearn import metrics
from sklearn.metrics import classification_report

"""# Reading dataset"""

# The dataset has been uploaded to my drive, then the dataset has been re-organized.
dataset= pd.read_csv('/content/gdrive/My Drive/cora/cora.content', sep="\t")
print (dataset)
dataset.columns = ['features'+str(i) for i in range(0,1435)]
# dataset=dataset.set_index('features0')
dataset

"""# Defining features and the label"""

X = dataset.iloc[:, 1:-2].values
y = dataset. iloc [:, -1].values

print("Matrix of features", X, sep='\n')
print("--------------------------------------------------")
print("Target Variable", y, sep='\n')

"""# Applying ML algorithm along with 10-fold cross validation"""

lr = LogisticRegression(solver='lbfgs', random_state=7)
skf = StratifiedKFold(n_splits=10,shuffle=True, random_state=7)
lst_accu_stratified = []
  
for i, (train_index, test_index) in enumerate (skf.split(X, y)):
    X_train_fold, X_test_fold = X[train_index], X[test_index]
    y_train_fold, y_test_fold = y[train_index], y[test_index]
    lr.fit(X_train_fold, y_train_fold)
    lst_accu_stratified.append(lr.score(X_test_fold, y_test_fold))
    print(f"Fold {i}:")
    print(f"  Test:  index={test_index}", y_test_fold)

# Print the output.
print('List of possible accuracy:', lst_accu_stratified)
print('\nMaximum Accuracy That can be obtained from this model is:',
      max(lst_accu_stratified)*100, '%')
print('\nMinimum Accuracy:',
      min(lst_accu_stratified)*100, '%')
print('\nOverall Accuracy:',
      mean(lst_accu_stratified)*100, '%')
print('\nStandard Deviation is:', stdev(lst_accu_stratified))
################################################################

"""# Defining the index"""

import re
paper_Index= f"{test_index}"
paper_Index = re.findall('\d+', paper_Index) 
paper_Index = np.array(paper_Index, dtype='int64')

paper_ID=[]

for i in paper_Index:
  paper_ID.append(dataset.loc[i].features0)

final_result = np.stack((paper_ID, y_test_fold), axis=1)
final_result

"""# Store predictions in TSV file"""

# Organized as `<paper_id> <class_label>
df = pd.DataFrame(final_result, columns=['paper_id','class_label'])
df.to_csv('results.tsv', index=False, sep='\t')

"""# Evaluate the approach"""

#The disadvantage of *subset accuracy* (also known as exact match ratio) measure is that multi-class classification problems have a chance of being partially correct, but here we ignore those partially correct matches.
#There is a function in scikit-learn which implements subset accuracy, called as accuracy_score that has beem imported earlier and used here.


predictions = lr.predict(X_test_fold)

print('Accuracy:', metrics.accuracy_score(y_test_fold, predictions))
print('Recall:',metrics.recall_score(y_test_fold, predictions, pos_label='positive',average='micro'))
print('Precision:',metrics.precision_score(y_test_fold, predictions,average='micro'))
print('CL Report:',metrics.classification_report(y_test_fold, predictions))