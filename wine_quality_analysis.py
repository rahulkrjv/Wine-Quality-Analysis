import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Define a function to concatenate the red and white wine datasets
def join(temp1, temp2):
    temp1['color'] = 'r'    # Add 'r' in the color column for 'Red wine'
    temp2['color'] = 'w'    # Add 'w' in the color column for 'White wine'
    return pd.concat([temp1, temp2])

# Load the red and white wine datasets
red = pd.read_csv("winequality-red.csv", sep = ';')
white = pd.read_csv("winequality-white.csv", sep = ';')

# Remove duplicate rows in both datasets
red = red.drop_duplicates()
white = white.drop_duplicates()

# Combine red and white wine datasets
wine = join(red.copy(), white.copy())

# Display summary statistics for red wine dataset
red_des = red.describe()
print("Red Wine Description:\n", red_des)

# Display summary statistics for white wine dataset
white_des = white.describe()
print("\nWhite Wine Description:\n", white_des)

# Display summary statistics for the combined wine dataset
wine_des = wine.describe()
print("\nCombined Wine Description:\n", wine_des)

# Create pair plots to visualize relationships between features and wine quality for red wine
sns.pairplot(red, hue='quality')
plt.title('Pair Plot for Red Wine')
plt.show()

# Create pair plots to visualize relationships between features and wine quality for white wine
sns.pairplot(white, hue='quality')
plt.title('Pair Plot for White Wine')
plt.show()

# Create pair plots to visualize relationships between features and wine quality for combined wine dataset
sns.pairplot(wine, hue='quality')
plt.title('Pair Plot for Combined Wine Dataset')
plt.show()

# Create a histogram to visualize the distribution of wine quality scores
plt.figure(figsize=(8, 5))
sns.histplot(wine['quality'], bins=range(1, 11), kde=True)
plt.xlabel('Wine Quality')
plt.ylabel('Frequency')
plt.title('Distribution of Wine Quality Scores')
plt.show()

# Compute the correlation matrix and create a heatmap
correlation_matrix = wine.drop(columns=['color']).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix[['quality']], annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Between Features and Wine Quality')
plt.show()

# Identify important factors influencing wine quality using Random Forest Regressor
# Separate features (X) and target (y)
X = wine.drop(columns=['color']).drop('quality', axis=1)
y = wine['quality']

# Train a Random Forest Regressor model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Get feature importances
feature_importances = model.feature_importances_

# Create a DataFrame to visualize feature importances
imp_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})
imp_df = imp_df.sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(data=imp_df, x='Importance', y='Feature', palette='viridis')
plt.title('Feature Importance for Wine Quality Prediction')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()
