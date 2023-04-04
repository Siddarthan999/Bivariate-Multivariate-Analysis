import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("FlightInformation.xlsx")
# Explore the dataset
print(df.head())
print(df.info())

# Define variable types
numerical_vars = ['Duration', 'Price']
categorical_vars = ['Airline', 'Source', 'Destination', 'Route', 'Total_Stops', 'Additional_Info']
ordinal_vars = []

#(i) Numerical & Numerical Analysis:
# Scatter plot
sns.scatterplot(x='Duration', y='Price', data=df)
plt.title('Scatter Plot - Duration vs Price')
plt.show()

# Correlation matrix
corr_matrix = df[numerical_vars].corr()
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix - Numerical Variables')
plt.show()

#(ii) Numerical & Categorical Analysis:
# Box plot
sns.boxplot(x='Airline', y='Price', data=df)
plt.title('Box Plot - Airline vs Price')
plt.show()

# Violin plot
sns.violinplot(x='Total_Stops', y='Price', data=df)
plt.title('Violin Plot - Total Stops vs Price')
plt.show()

#Multivariate Analysis:
# Pair plot
sns.pairplot(df[numerical_vars], kind='reg')
plt.suptitle('Pair Plot - Numerical Variables')
plt.show()

# Heatmap
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Heatmap - All Variables')
plt.show()
