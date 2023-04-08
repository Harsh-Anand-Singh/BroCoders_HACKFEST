import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier

cols_names = ['Department','Semester', 'p1','p2','p3','p4','p5', 'Course']

course_data=pd.read_csv('course_preferences.csv',header=None,names=cols_names)

feature_cols = ['Department','Semester', 'p1','p2','p3','p4','p5']

X=course_data[feature_cols]

Y=course_data.Course

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

clf = DecisionTreeClassifier()

clf = clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# for i in y_pred :
#   print("your alloted course is ") 
#   print(i) 
#print(y_pred)