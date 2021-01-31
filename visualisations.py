from datetime import date

from pandas import read_csv
import pandas as pd
from matplotlib import pyplot
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn

series = read_csv('sentiments_only_text_and_score3.csv', header=0, index_col=0, parse_dates=True, squeeze=False)
print(series.head(5))
davg = series.resample('D').mean()
print(davg)
davg.plot(y=['Sentiment', 'Vader', 'TextBlob'])
pyplot.xlabel("Tweet date")
pyplot.ylabel("Sentiment polarity")
# pyplot.plot()

#########  LDA
datadf = pd.read_csv('linearegressionfile', sep=",", header=0)

datadf['date_ordinal'] = pd.to_datetime(datadf['created_at']).apply(lambda date: date.toordinal())
print(datadf)

ax = seaborn.regplot(data=datadf, x='date_ordinal', y='Sentiment')
ax.set_xlim(datadf['date_ordinal'].min() - 1, datadf['date_ordinal'].max() + 1)
ax.set_ylim(0, datadf['Sentiment'].max() + 1)
ax.set_xlabel('date')
new_labels = [date.fromordinal(int(item)) for item in ax.get_xticks()]
ax.set_xticklabels(new_labels)
pyplot.show()

#
# # X = list(range(1, 42))
# # Y =
# X = list(range(1, 43))
# Y = davg['Sentiment']
#
# print(X)
# print(Y)
# linear_regressor = LinearRegression()  # create object for the class
#
# linear_regressor.fit(X = X, y= Y)
# pyplot.show()

# pyplot.savefig("plot2.png")
