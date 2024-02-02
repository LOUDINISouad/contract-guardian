import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import ast

# Load the data
data = pd.read_csv('data.csv')

# Convert string representations of lists to actual lists
data['padded_arrays'] = data['padded_arrays'].apply(lambda x: ast.literal_eval(x.replace("...", "")))

# Extract features (X) and target variable (y)
X = data["padded_arrays"]
y = data["contract_type"] == "valid"

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Assuming you have numeric representations of your padded arrays, you may need to reshape them
# X_train = np.array(X_train.values.tolist())
# X_test = np.array(X_test.values.tolist())
"""
# Create an instance of the Logistic Regression model
logisticRegr = LogisticRegression()

# Train the model
logisticRegr.fit(X_train.tolist(), y_train)

# Make predictions on the test set
y_pred = logisticRegr.predict(X_test.tolist())

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Display additional metrics
print(classification_report(y_test, y_pred))
"""