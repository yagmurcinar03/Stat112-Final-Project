# import necessary libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the DataFrame
laptops_data = pd.read_excel('temizdata8.xlsx')

# Adjusting the visualizations with pastel tones for all the questions

# Question 1: Average Laptop Price Over The Years
filtered_data = laptops_data[laptops_data['Year'].isin([2020, 2021, 2022, 2023])]
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data, x='Year', y='Price', estimator='mean', color='darkseagreen')
plt.title('Average Laptop Price Over The Years')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.xticks([2020, 2021, 2022, 2023])
plt.grid(True)
plt.show()

# Question 2: Price Variation by Condition and Brand
grouped_data = laptops_data.groupby(['Brand', 'Condition'])['Price'].mean().unstack().fillna(0)
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='Pastel2')
plt.title('Price Variation by Condition and Brand')
plt.xlabel('Brand')
plt.ylabel('Average Price')
plt.legend(title='Condition')
plt.grid(axis='y')
plt.show()

# Question 3: Average Display Size by Brand
grouped_brands = laptops_data.groupby('Brand')['Display Size'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Brand', y='Display Size', data=grouped_brands, palette='Pastel2')
plt.title('Average Display Size by Brand')
plt.xticks(rotation=45)
plt.xlabel('Brand')
plt.ylabel('Average Display Size (inches)')
plt.show()

# Question 4: Distribution of Laptop Weights
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 2)
sns.histplot(laptops_data['Weight'], color='beige')
plt.title("Distribution of Laptop Weights")
plt.show()

# Question 5: Price Distribution by Processor
plt.figure(figsize=(12, 8))
sns.boxplot(data=laptops_data, x='Processor', y='Price', palette='Pastel2')
plt.title('Price Distribution by Processor')
plt.xlabel('Processor')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
