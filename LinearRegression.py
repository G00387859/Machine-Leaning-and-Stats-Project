# Import linear_model from sklearn.
import sklearn.linear_model as lm
# Let's use pandas to read a csv file and organise our data.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# read the dataset
#df = pd.read_csv('https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv')
df =pd.read_csv('powerproduction.csv')
# Plots styles.
plt.style.use('ggplot')
# Plot size.
plt.rcParams['figure.figsize'] = (14, 10)
# Create a linear regression model instance.
m = lm.LinearRegression()
df.isnull().sum()
x=df[["speed","power"]]
y=df["power"]
m.fit(x,y)
m.intercept_
m.coef_
m.score(x,y)
z=df["speed"]
q=df["power"]
np.polyfit(z,q,1)
m,c =np.polyfit(z,q,1)
a,b,c,d = np.polyfit(z,q,3)

def findy(x):
    print('x =',x)
    y = (a*x**3) + (b*x**2) + (c*x) +d
    return '{:.2f}'.format(y)
print('y = ', findy(10))