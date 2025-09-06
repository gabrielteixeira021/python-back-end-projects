# library imports
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load Irirs dataset
iris = load_iris(as_frame=True)
X, y = iris.data, iris.target

# separates data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Initializes and train the KNN model
model = KNeighborsClassifier(n_neighbors=10)
model.fit(X_train, y_train)

# evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Saves the model
joblib.dump(model, 'knn_iris_model.pkl')
print("Model saved as 'knn_iris_model.pkl'")