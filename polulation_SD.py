import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

def random_set_of_means(counter):
    datafile = pd.read_csv("data.csv")
    data =datafile["average"].tolist()
    dataset = []
    for i in range (0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    datafile= mean_list
    fig = ff.create_distplot([datafile], ["average"], show_hist=False)
    fig.add_trace(go.Scatter(x=[average, average], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def Standard_deviation ():
    meanlist= []
    for i in range (0,1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print( "Standard Deviation of sampling mean :- ", std_deviation)
    show_fig()

Standard_deviation()
