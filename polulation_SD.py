import plotly.figure_factory as ff
import plotly.graph_object as go
import statistics
import random
import pandas as pd 
import csv

def random_set_of_means(counter):
    datafile = pd.read_csv("data.csv")
    data =datafile["temp"].tolist()
    dataset = []
    for i in rande (0, counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    datafile= mean_list
    fig = ff.create_distplot([data], ["temp"], show_hist=False)
    ffig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
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
