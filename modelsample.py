import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data from a CSV file
df = pd.read_csv('data.csv')

# Preprocess the data by converting categorical variables to one-hot encoded features
semester_enc = OneHotEncoder(categories=[range(1, 11)])
semester_enc.fit(df[['Semester']])
semester_onehot = semester_enc.transform(df[['Semester']])
semester_onehot_df = pd.DataFrame(semester_onehot, columns=[f"Semester_{i}" for i in range(1, 11)])

department_enc = OneHotEncoder(categories=[['Civil', 'Computer Science', 'Electrical', 'Mechanical', 'Mining']])
department_enc.fit(df[['Department']])
department_onehot = department_enc.transform(df[['Department']])
department_onehot_df = pd.DataFrame(department_onehot, columns=department_enc.get_feature_names(['Department']))

preference_enc = OneHotEncoder(categories=[f"Subject {i}" for i in range(1, 21)])
preference_enc.fit(df[['Preference 1', 'Preference 2', 'Preference 3', 'Preference 4', 'Preference 5']])
preference_onehot = preference_enc.transform(df[['Preference 1', 'Preference 2', 'Preference 3', 'Preference 4', 'Preference 5']])
preference_onehot_df = pd.DataFrame(preference_onehot, columns=[f"Preference {i}" for i in range(1, 101)])

# Combine the one-hot encoded features into a single dataframe
df_processed = pd.concat([semester_onehot_df, department_onehot_df, preference_onehot_df], axis=1)

# Split the data into training and testing sets
X = df_processed.iloc[:, :-1]  # All columns except for the target column
y = df_processed.iloc[:, -1]   # Only the target column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

# Make predictions on the test data and evaluate the accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
