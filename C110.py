import pandas as pd 
import csv
import random
import statistics
import plotly.figure_factory as ff 
df=pd.read_csv('newdata.csv')
data=df['average'].tolist()
populationMean=statistics.mean(data)
populationStd=statistics.stdev(data)
print(populationMean)
print(populationStd)
fig=ff.create_distplot([data],['average'],show_hist=False)
fig.show()