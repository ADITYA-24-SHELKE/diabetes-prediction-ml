import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
df = pd.read_csv('diabetes.csv')


# print(df.head())


# print(df.shape)      # rows, columns
# print(df.columns)    # column names
# print(df.info())     # data types
# print(df.isnull().sum())

# cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

# df[cols] = df[cols].replace(0, np.nan)

X = df.drop("Outcome", axis=1)   # features
y = df["Outcome"]               # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

model = SVC(kernel='rbf')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

joblib.dump(model, "diabetes_model.pkl")

# save scaler (VERY IMPORTANT for SVM)
joblib.dump(scaler, "scaler.pkl")

print("Model saved successfully!")