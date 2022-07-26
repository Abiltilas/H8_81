import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
from PIL import Image # converting images into arrays
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts
import seaborn as sns
!pip install wordcloud
# import package and its set of stopwords
from wordcloud import WordCloud, STOPWORDS

mpl.style.use('ggplot') # optional: for ggplot-like style

# check for latest version of Matplotlib
print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0

df = pd.read_csv('ds_salaries.csv')

print(len(df))

print(df.shape) 

print(df.head())

#Info summary
print("Summary:")
print(df.describe())

#Jumlah per masing2 pekerjaan
print("Jumlah per masing2 Pekerjaan:")
print(df.job_title.value_counts())

#Barplot, RegressionPlot
x_var = df['experience_level'].values
y_var = df['salary'].values
sns.barplot(x=x_var, y=y_var, data=df)
sns.regplot(x=x_var, y=y_var, data=df)
plt.xticks(rotation=45)
print()

#Diagram Waffle

# compute the proportion of each category with respect to the total
total_values = sum(df['salary_in_usd'])
category_proportions = [(float(value) / total_values) for value in df['salary']]


width = 40 # width of chart
height = 10 # height of chart

total_num_tiles = width * height # total number of tiles

print ('Total number of tiles is ', total_num_tiles)

# compute the number of tiles for each catagory
tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

# initialize the waffle chart as an empty matrix
waffle_chart = np.zeros((height, width))

# define indices to loop through waffle chart
category_index = 0
tile_index = 0

# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1       
            
        # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index
        
print ('Waffle chart populated!')
    
# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

#Regression Plot



