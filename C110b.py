import pandas as pd 
import csv
import random
import statistics
import plotly.figure_factory as ff 
df=pd.read_csv('newdata.csv')
data=df['average'].tolist()
populationMean=statistics.mean(data)
populationStd=statistics.stdev(data)
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    std=statistics.stdev(dataSet)
    return mean

def showFig(meanList):
    df=meanList
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.show()

def setUp():
    meanList=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)
setUp()