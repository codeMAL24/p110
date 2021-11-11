import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random 

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
mean = s.mean(data)
std = s.stdev(data)

def showFig(meanList):
    df = meanList
    mean = s.mean(df)
    fig = ff.create_distplot([df],["READING TIME"], show_hist=False)
    fig.show()

def rsom(counter):
    dataSet = []
    for i in range(0,counter):
        r = random.randint(0,len(data)-1)
        value = data[r]
        dataSet.append(value)
    mean = s.mean(dataSet)
    return mean

def setup():
    mlist = []
    for i in range(0,100):
        som = rsom(30)
        mlist.append(som)
    showFig(mlist)
    m = s.mean(mlist)
    print(f"mean of sampling distribution{m}")    
    std = s.stdev(mlist)
    print(f"std of sampling distribution{std}") 
setup()  
