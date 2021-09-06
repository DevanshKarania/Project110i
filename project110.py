import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("class110/data1.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
print(mean)

dataSet=[]

def random_setOf_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        setOfMeans = random_setOf_mean(30)
        mean_list.append(setOfMeans)
    
    show_fig(mean_list)

setup()