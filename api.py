# importing libraries
import requests
import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import matplotlib.pyplot as plt


# Loading the env file
load_dotenv()
# load_dotenv(find_dotenv())

api_key= os.getenv('api_key')

# Set up variables
#api_key = '053fb67bfeb8479f36f9522077402043'

# list of cities to get the data for 
cities = ['Auckland', 'Sydney', 'Tokyo', 'New York', 'London', 'Paris', 'Berlin', 'Moscow', 'Beijing', 'Mumbai']

# Initialise an empty list to store the data 
weather_data = []

# Loop through the list of cities to make API calls
for city in cities:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        # Add the response data to the list
        weather_data.append(response.json())
    else:
        print('Failed to retrieve data')


# Convert the list of data to pandas dataframe
df = pd.DataFrame(weather_data)
df.head()

# Perform analysis on the dataframe
# example to get the average temperature of all cities
df['temp_avg'] = df['main'].apply(lambda x: x['temp'])
print(f"Average temperature across cities: {df['temp_avg'].mean()} Kelvin")

# To analyze data specifically for Auckland
auckland_data = df[df['name'] == 'Auckland']
print(f"Auckland weather data: {auckland_data}")

# Visualisation
# Convert temperatures from Kelvin to Celsius for better understanding
df['temp_celsius'] = df['temp_avg'].apply(lambda x: x - 273.15)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['name'], df['temp_celsius'], color='skyblue')
plt.xlabel('City')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Temperature Comparison Among Cities')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
plt.show()
