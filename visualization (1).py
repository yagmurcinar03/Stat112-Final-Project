
# read the excel file
laptops_data = pd.read_excel('temizdata8.xlsx')

# import pandas, matplotlib and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Question 1. How does the average price of laptops change over the years from 2020 to 2023?

# construct a line plot
# filter the data for the specified years (2020-2023)
filtered_data = laptops_data[laptops_data['Year'].isin([2020, 2021, 2022, 2023])]

# calculate average laptop price from 2020 to 2023 and choose a theme
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data, x='Year', y='Price', estimator='mean', color='darkseagreen')


# choose titles and assign values of x-axis
plt.title('Average Laptop Price Over The Years')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.xticks([2020, 2021, 2022, 2023])

# add grid
plt.grid(True)

# display the plot
plt.show()


# Question 2. In which way does condition affect prices based on brands?

# construct a stacked bar plot
# calculate the average price by condition for each brand
grouped_data = laptops_data.groupby(['Brand', 'Condition'])['Price'].mean().unstack().fillna(0)

# make it stacked and assign the size, theme and titles
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8), colormap = 'Pastel2' )


plt.title('Price Variation by Condition and Brand')
plt.xlabel('Brand')
plt.ylabel('Average Price')
plt.legend(title='Condition')

# add grid
plt.grid(axis='y')

# display the plot
plt.show()

# Question 3. How does display size vary among brands?

# construct a bar plot
# set x-axis to brand and y-axis to average display size 
grouped_brands = laptops_data.groupby('Brand')['Display Size'].mean().reset_index()

# choose size, color and titles
plt.figure(figsize=(10, 6))
sns.barplot(x='Brand', y='Display Size', data=grouped_brands, palette='Pastel2')
plt.title('Average Display Size by Brand')
plt.xticks(rotation=45)
plt.xlabel('Brand')
plt.ylabel('Average Display Size (inches)')

# display the plot
plt.show()

# Question 4. Which weight of laptops are prefered more by users?

# construct a histogram
# define size
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 2)

# define title, variable and color and draw the histogram
sns.histplot(laptops_data['Weight'], color='beige')
plt.title("Distribution of Laptop Weights")

# Question 5. How processors affect laptop's costs?

# construct box plots for each processor
# define size, variables and colors
plt.figure(figsize=(12, 8))
sns.boxplot(data=laptops_data, x='Processor', y='Price', palette='Pastel2')

# define titles
plt.title('Price Distribution by Processor')
plt.xlabel('Processor')
plt.ylabel('Price')

# choose rotation of processor names and add grid
plt.xticks(rotation=45)
plt.grid(True)

# display the plot
plt.show()      