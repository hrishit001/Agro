
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset
data = pd.read_csv("crop_data_india_500.csv")

le_state = LabelEncoder()
le_city = LabelEncoder()

data['State_encoded'] = le_state.fit_transform(data['State'])
data['City_encoded'] = le_city.fit_transform(data['City'])

features = ['temperature', 'humidity', 'rainfall',
            'State_encoded', 'City_encoded']
X = data[features]
y = data['Crop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=120, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nClassification Report:\n", classification_report(y_test, y_pred))


joblib.dump(model, "crop_prediction_model_district.joblib")
joblib.dump((le_state, le_city), "encoders.joblib")
print("\nModel and encoders saved successfully!")


example = [[12, 45, 4200,
            le_state.transform(['Uttar Pradesh'])[0],
            le_city.transform(['Lucknow'])[0]]]

pred_crop = model.predict(example)
print(f"\nPredicted Crop: {pred_crop[0]}")
importances = model.feature_importances_
feature_names = X.columns


indices = np.argsort(importances)[::-1]

print("\nFeature Importance Ranking:")
for i in range(len(feature_names)):
    print(f"{i+1}. {feature_names[indices[i]]}: {importances[indices[i]]:.4f}")


plt.figure(figsize=(8, 5))
plt.title("Feature Importance in Crop Prediction Model")
plt.bar(range(len(importances)), importances[indices], color='forestgreen', align="center")
plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45, ha="right")
plt.tight_layout()
plt.show()
