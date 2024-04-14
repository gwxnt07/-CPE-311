# -*- coding: utf-8 -*-
"""Midterm Skills Exam: Data Wrangling and Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xlHYArHdz6sN93gjqlOy0YU8bZ0hYQkZ
"""

pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
census_income = fetch_ucirepo(id=20)

# data (as pandas dataframes)
X = census_income.data.features
y = census_income.data.targets

# metadata
print(census_income.metadata)

# variable information
print(census_income.variables)

print("First few rows of the dataset:")
print(X.head())

print("\nSummary of the dataset:")
print(X.info())  # Changed from df.info()

print("\nDescriptive statistics:")
print(X.describe())  # Changed from df.describe()))

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fetch the dataset
from ucimlrepo import fetch_ucirepo
census_income = fetch_ucirepo(id=20)
X = census_income.data.features
y = census_income.data.targets

print(census_income.metadata)
print(census_income.variables)

X.replace('?', np.nan, inplace=True)
X.dropna(inplace=True)  # or you could use an imputation strategy

X = pd.get_dummies(X)

X.hist(bins=15, figsize=(15, 10))
plt.show()

for column in X.select_dtypes(include=[np.number]).columns:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=X[column])
    plt.show()

plt.figure(figsize=(12, 10))
sns.heatmap(X.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.show()

print(X.columns)

# If 'y' is a series and should be used as the 'hue', you might need to add it back to the dataframe or adjust your code.
X['income'] = y  # Only do this if it makes sense for your analysis; otherwise, handle separately.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='income', data=X, hue='income')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Example: Plotting the distribution of 'age'
plt.figure(figsize=(10, 6))
sns.histplot(data=X, x='age', bins=30, kde=True)  # Assuming 'age' is a column in your DataFrame X
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

print(X.columns)

plt.figure(figsize=(10, 6))
sns.countplot(data=X, x='education-num')  # Using 'education-num' instead of 'education'
plt.title('Distribution of Education Levels')
plt.xlabel('Education Level (Numerical)')
plt.ylabel('Counts')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='income', y='hours-per-week', data=X)
plt.title('Hours Worked per Week by Income Level')
plt.xlabel('Income Level')
plt.ylabel('Hours per Week')
plt.show()

numeric_columns = X.select_dtypes(include=['number'])
correlation_matrix = numeric_columns.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap of Numerical Features')
plt.show()

subset = X[['age', 'hours-per-week', 'education-num', 'income']]  # Adjust column names as needed
sns.pairplot(subset, hue='income', diag_kind='kde', markers=["o", "s"])  # Ensure 'income' is available or adjust accordingly
plt.title('Pair Plot of Age, Hours per Week, and Education Level')
plt.show()

