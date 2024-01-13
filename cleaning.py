# import pandas and numpy libraries
import pandas as pd
import numpy as np
import seaborn as sns


# drop first two row and first three columns which are unnecessary
laptops_excel = pd.read_excel("Laptop_Prices.xlsx", header=2)
laptops_excel = laptops_excel.iloc[:, 3:]

# display first-last five rows and general view of the data
laptops_excel.head()
laptops_excel.tail()
laptops_excel.info()

# remove unnnecessary marks in the headers and rename
laptops_excel.columns = laptops_excel.columns.str.title()
laptops_excel.columns
laptops_excel.columns = laptops_excel.columns.str.strip('"')
laptops_excel = laptops_excel.rename({'Ram': 'Ram(GB)', 'Storage': 'Storage(GB)', 'Id': 'ID', '##3Displaysize': 'Display Size', '$$Price': 'Price', '##Weight': 'Weight'},axis = "columns")
laptops_excel.columns

# check missing values in the data and their percentages
new_df = pd.DataFrame(laptops_excel.isnull().sum())
new_df.columns = ['Missing Number']
new_df['Missing Percentage'] = (new_df['Missing Number']*100)/laptops_excel.shape[0]
print(new_df['Missing Percentage'])

# check number of duplicates and remove them
laptops_excel.duplicated().sum()
laptops_excel = laptops_excel.drop_duplicates()
laptops_excel.duplicated().sum()

# tidy the unit and marks for Storage and Ram
laptops_excel['Ram(GB)'] = laptops_excel['Ram(GB)'].str.replace("-","", regex=True)
laptops_excel['Storage(GB)'].loc[laptops_excel['Storage(GB)'] == '1TB'] = '1024GB'
laptops_excel['Storage(GB)'] = laptops_excel['Storage(GB)'].str.replace("GB","", regex=True)
laptops_excel['Ram(GB)'] = laptops_excel['Ram(GB)'].str.replace("GB","", regex=True)

median_value = laptops_excel['Storage(GB)'].median()
# convert the data types of Storage and Ram to proper form
laptops_excel['Storage(GB)'] = laptops_excel['Storage(GB)'].astype(float)
laptops_excel['Ram(GB)'] = laptops_excel['Ram(GB)'].astype(float)
laptops_excel['Ram(GB)'] = laptops_excel['Ram(GB)'].fillna(0).astype(int)
laptops_excel['Storage(GB)'] = laptops_excel['Storage(GB)'].fillna(median_value).astype(int)

# tidy the spelling of the values of Brand column 
laptops_excel['Brand'].loc[laptops_excel['Brand'] == 'Hp'] = 'HP'
laptops_excel['Brand'].loc[laptops_excel['Brand'] == 'APPLE'] = 'Apple'
laptops_excel['Brand'].loc[laptops_excel['Brand'] == 'dell'] = 'Dell'

# check whether all strings in same format
laptops_excel['Brand'].value_counts()
laptops_excel['Processor'].value_counts()
laptops_excel['Ram(GB)'].value_counts()
laptops_excel['Storage(GB)'].value_counts()
laptops_excel['Graphics'].value_counts()
laptops_excel['Condition'].value_counts()
laptops_excel['Year'].value_counts()

# make all values in Condition columns in title format
laptops_excel['Condition'].loc[laptops_excel['Condition'] == ' Refurbished'] = 'Refurbished'
laptops_excel['Condition'].loc[laptops_excel['Condition'] == 'refurbished'] = 'Refurbished'
laptops_excel['Condition'].loc[laptops_excel['Condition'] == 'USED'] = 'Used'

laptops_excel.describe()

# fill the na values in Storage column with median
median_value = laptops_excel['Storage(GB)'].median()
laptops_excel['Storage(GB)'].fillna(median_value)

# fill the na values in Graphics column with mode
mode_graphics = laptops_excel['Graphics'].mode()[0]
laptops_excel['Graphics'] = laptops_excel['Graphics'].fillna(mode_graphics)

# change the commas to point to convert string values to float in Display Size column
laptops_excel['Display Size'] = laptops_excel['Display Size'].str.replace(",",".").fillna(laptops_excel['Display Size'])
laptops_excel['Display Size'] = laptops_excel['Display Size'].astype(float)

# detect outliers if there are any in Display Size column
Q1 = laptops_excel['Display Size'].quantile(0.25)
Q3 = laptops_excel['Display Size'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = laptops_excel[(laptops_excel['Display Size'] < lower_bound) | (laptops_excel['Display Size'] > upper_bound)]
num_outliers = outliers.shape[0]
print("Number of outliers display size:", num_outliers)
print(outliers)

# fill the na values with mean because of there is no outlier in Display Size column
mean = laptops_excel['Display Size'].mean()
laptops_excel['Display Size'].fillna(mean, inplace=True)

# fill the na vaules with mode in Condition column
laptops_excel['Condition'] = laptops_excel['Condition'].fillna(laptops_excel['Condition'].mode()[0])

# detect outliers if there are any in Price column
Q1 = laptops_excel['Price'].quantile(0.25)
Q3 = laptops_excel['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = laptops_excel[(laptops_excel['Price'] < lower_bound) | (laptops_excel['Price'] > upper_bound)]

num_outliers = outliers.shape[0]
print("Number of outliers:", num_outliers)
print(outliers)

# fill the na values with median because of there are outliers in Price column
median_price = laptops_excel['Price'].median()
laptops_excel['Price'].fillna(median_price, inplace=True)


Q1 = laptops_excel['Price'].quantile(0.25)
Q3 = laptops_excel['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# fill the outliers with rounded mean in Price column
mean_price = laptops_excel['Price'].dropna().mean()
laptops_excel.loc[laptops_excel['Price'] < lower_bound, 'Price'] = round(mean_price)
laptops_excel.loc[laptops_excel['Price'] > upper_bound, 'Price'] = round(mean_price)

# convert the data types of Price to integer
laptops_excel['Price'] = laptops_excel['Price'].fillna(0).astype(int)



# change the commas to point to convert string values to float in Weight column
laptops_excel['Weight'] = laptops_excel['Weight'].str.replace(",",".").fillna(laptops_excel['Weight'])
laptops_excel['Weight'] = laptops_excel['Weight'].astype(float)

# detect outliers if there are any in Weight column
Q1 = laptops_excel['Weight'].quantile(0.25)
Q3 = laptops_excel['Weight'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = laptops_excel[(laptops_excel['Weight'] < lower_bound) | (laptops_excel['Weight'] > upper_bound)]

num_outliers = outliers.shape[0]
print("Number of outliers:", num_outliers)

print(outliers)

# fill the na values with mean because of there is no outlier in Weight column
mean_weight = round(laptops_excel['Weight'].mean(),1)
laptops_excel['Weight'].fillna(mean_weight, inplace=True)

# make sure that the data is clean and tidy 
laptops_excel.isnull().sum()
laptops_excel.info()

# examine the descriptive statistics of the variables
round(laptops_excel.describe())
laptops_excel.head(50)

# download the clean data file
laptops_excel.to_excel("temizdata8.xlsx", index=False)


