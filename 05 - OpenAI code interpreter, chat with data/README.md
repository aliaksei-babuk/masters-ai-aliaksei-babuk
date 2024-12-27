# masters-ai

In nex table london_houses we have Columns:

Address: The address of the house.
Neighborhood: The neighborhood or district where the house is located.
Bedrooms: The number of bedrooms in the house.
Bathrooms: The number of bathrooms in the house.
Square Meters: The total size of the house in square meters.
Building Age: The age of the building, indicating how long ago it was constructed.
Garden: Indicates whether the house has a garden ("Yes" or "No").
Garage: Indicates whether the house has a garage ("Yes" or "No").
Floors: The total number of floors in the house.
Property Type: The type of property, such as "Apartment" or "House."
Heating Type: The type of heating system used in the house (e.g., "Central Heating," "Gas").
Balcony: Indicates whether the house has a balcony ("Yes" or "No").
Interior Style: The interior design style of the house (e.g., "Modern," "Contemporary").
View: The type of view from the house (e.g., "City View," "Sea View").
Materials: The materials used in the construction of the house (e.g., "Brick," "Wood").
Building Status: The current condition of the building (e.g., "New," "Renovated," "Old").
Price (£): The sale price of the house, in British pounds (£).

Using matplotlib, create a histogram to show the correlation between the number of bedrooms, bathrooms, square feet, metres, building age and how they correlate with price.


The dataset appears to be well-structured and includes the relevant columns for analysis. Let's create histograms to visualize the correlation between price and other numerical features: Bedrooms, Bathrooms, Square Meters, and Building Age.

First, I'll ensure the dataset's columns have the correct data types for numerical analysis, then plot the histograms.

import pandas as pd

# Load the CSV file to inspect its structure
file_path = '/mnt/data/london_houses.csv'
london_houses_df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
london_houses_df.head()
[picture]
The scatter plots illustrate how the Price (£) correlates with the following features:

Bedrooms vs. Price: Shows a potential upward trend where more bedrooms are generally associated with higher prices.
Bathrooms vs. Price: Indicates a similar trend as with bedrooms, with properties having more bathrooms often priced higher.
Square Meters vs. Price: A clear positive correlation where larger properties (in terms of square meters) tend to have higher prices.
Building Age vs. Price: The relationship is less linear, suggesting age might influence price differently, perhaps depending on other factors like location or renovation status.