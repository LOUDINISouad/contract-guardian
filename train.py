import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv('data.csv')

X = data.loc[:, 'token_0':'token_9020']
y = data["contract_type"] == "valid"

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of the Logistic Regression model
logisticRegr = LogisticRegression()

# Train the model
logisticRegr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logisticRegr.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Display additional metrics
print(classification_report(y_test, y_pred))

