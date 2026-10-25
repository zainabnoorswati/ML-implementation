import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. Create the dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast'],
    'Wind':    ['Weak',  'Strong', 'Weak',     'Weak', 'Strong', 'Strong', 'Strong'],
    'Play':    ['No',    'No',     'Yes',      'Yes',  'No',     'No',     'Yes']
}
df = pd.DataFrame(data)

# 2. Encode text to numbers (One-Hot Encoding)
X = pd.get_dummies(df[['Outlook', 'Wind']])
y = df['Play']

# 3. Train the CART model
model = DecisionTreeClassifier(criterion='gini', random_state=42)
model.fit(X, y)

# 4. Predict a new instance
# Creating a new row: Sunny, Weak (matching the column order of X)
# X columns are: Outlook_Overcast, Outlook_Rain, Outlook_Sunny, Wind_Strong, Wind_Weak
new_instance = [[0, 0, 1, 0, 1]] 
prediction = model.predict(new_instance)
print(f"Prediction for Outlook=Sunny, Wind=Weak: {prediction[0]}")

# 5. Visualize the tree
plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.title("CART Decision Tree (Gini Impurity)")
plt.show()