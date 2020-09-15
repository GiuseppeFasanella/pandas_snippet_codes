import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt

df = pd.DataFrame(index=['9h30','10h','10h30','14h','16h'], columns=['10h30','11h','12h','16h','18h','19h'])
df.loc['9h30','16h']=0.491
df.loc['10h','16h'] = 0.527
df.loc['10h30','16h']=0.544
df.loc['9h30','10h30']=0.47
df.loc['10h','11h']=0.475
df.loc['10h','12h']=0.507
df.loc['14h','16h']=0.545
df.loc['16h','18h']=0.512
df.loc['16h','19h']=0.533

mask=df.isnull() ## I don't want to plot missing values
## Substitute nans with a value just above the "real" values you have
df = df.fillna(0.55) #Otherwise it is going to complain that there are nans
g = sns.heatmap(df, mask=mask, cmap="Oranges") #, vmin=0.46)
g.set_facecolor('xkcd:white')

# turn the axis label
plt.xlabel("close hour")
plt.ylabel("open hour")

for item in g.get_yticklabels():
    item.set_rotation(0)

# for item in g.get_xticklabels():
#     item.set_rotation(90)
