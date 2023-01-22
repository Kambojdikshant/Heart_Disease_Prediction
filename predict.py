import numpy as np 
import pandas as pd 
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

heart = pd.read_csv("Heart_data.csv") ; 

heart_df = heart.copy() 
heart_df = heart_df.rename(columns={'condition':'target'})
print(heart_df.head()) 

x = heart_df.drop(columns='target')
y = heart_df.target 

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=42)

scaler = StandardScaler() 
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.fit_transform(x_test) 

model = RandomForestClassifier(n_estimators=20)
model.fit(x_train_scaler,y_train)
y_pred = model.predict(x_test_scaler) 
p = model.score(x_test_scaler, y_test) 
print(p)

print('Classification Report\n',classification_report(y_test, y_pred))
print('Accuracy : {}%\n',format(round((accuracy_score(y_test,y_pred)*100),2)))

cm = confusion_matrix(y_test, y_pred)
print(cm)

filename = 'heart_predict_knn_model.pkl'
pickle.dump(model,open(filename,'wb'))
