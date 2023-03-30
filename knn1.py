import numpy as np
import pandas as pd
from sklearn import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('outflowset.csv')
data = df[["CurrentBalance","YearInflow","ManualTransactions","onlineTransactions","TotalTransactions","NoOfclosedAccounts","NewAccountsOpened","No.ofchequeBounces","No.of failedtransactions","YearOutflow","OverallPerspective"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1500]
training_outputs = outputs[:1500]
testing_inputs = inputs[1500:]
testing_outputs = outputs[1500:]
classifier = KNeighborsClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
from sklearn.metrics import recall_score
recallmicro = 100.0 *recall_score(testing_outputs, predictions,average='micro',zero_division=1)
print ("The recall_Score of KNN Classifier on testing data is: " + str(recallmicro))
testSet = [[96045730,34021170192,249168,257583726,257832894,138,2731,5252,758327,22241415950]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MLP prediction on the first test set is:',predictions)
testSet = [[41180533,57794202309,340947,874020505,874361452,952,6220,7405,5380871,17026153603]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MLP prediction on the second test set is:',predictions)
testSet = [[64265782,77824207077,980013,594929847,595909860,211,9439,44,1010145,79314294345]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MLP prediction on the third test set is:',predictions)
#In the output, 0 indicates 'High Failure Risk',1 indicates 'Medium Failure Risk',2 indicates 'Low Failure Risk'