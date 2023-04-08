import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

def sarsa(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    
    current_value = q_table[state][action]
    
    
    next_value = q_table[next_state][next_action]
    
    
    new_value = current_value + alpha * (reward + gamma * next_value - current_value)
    q_table[state][action] = new_value

    return q_table

cols_names = ['Department','Semester', 'p1','p2','p3','p4','p5', 'Course']
course_data=pd.read_csv('course_preferences.csv',header=None,names=cols_names)

feature_cols = ['Department','Semester', 'p1','p2','p3','p4','p5']
X = course_data[feature_cols].values
Y = course_data.Course.values

n_states = 100
n_actions = len(np.unique(Y))


q_table = np.zeros((n_states, n_actions))


epsilon = 0.1
alpha = 0.5
gamma = 0.9


prev_state = None
prev_action = None


for i in range(len(X)):
   
    state = int(sum(X[i]))
    

    if np.random.uniform(0, 1) < epsilon:
        action = np.random.choice(range(n_actions))
    else:
        action = np.argmax(q_table[state])
    
   
    if prev_state is not None:
        reward = int(action == Y[i])
        q_table = sarsa(q_table, prev_state, prev_action, reward, state, action, alpha, gamma)
    
   
    prev_state = state
    prev_action = action


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


custom = [[3,2,5,3,1,8,10]]
state = int(sum(custom[0])/2)
action = np.argmax(q_table[state])
user_pred = action
print(f"RESULT: {user_pred}")