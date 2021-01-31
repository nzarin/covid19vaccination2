import pandas as pd
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("task2_data.csv")
colors = ['red', 'yellow', 'green']
labels = ['negative', 'neutral', 'positive']

nr_relevants = df['relevanceJudge'] == 1
nr_irrelevants = df['relevanceJudge'] == 0
nr_geo_trues = df['isGeoEnabled'] == 1
nr_geo_falses = df['isGeoEnabled'] == 0

nr_geo_true_relevant = df[nr_relevants & nr_geo_trues]
nr_geo_false_relevant = df[nr_relevants & nr_geo_falses]
nr_geo_true_irrelevant = df[nr_irrelevants & nr_geo_trues]
nr_geo_false_irrelevant = df[nr_irrelevants & nr_geo_falses]

data_geo_relevant = [len(nr_geo_true_relevant), len(nr_geo_false_relevant)]
data_geo_irrelevant = [len(nr_geo_true_irrelevant), len(nr_geo_false_irrelevant)]

print("###################")
print(data_geo_relevant)
print(data_geo_irrelevant)
print("####################")

fig = plt.figure()
# fig.set_tight_layout(False)
ax = fig.add_axes([0, 0, 1, 1])
langs = ['Geo enabled', 'Geo disabled']

# if interested in relevant
# ax.bar(langs, data_geo_relevant)
# plt.title("Relevant")
# plt.savefig('rel-fig.png', bbox_inches='tight')

# if interest in irrelevant
ax.bar(langs, data_geo_irrelevant)
plt.title("Irrelevant")
plt.savefig('irrel-fig.png',bbox_inches='tight')

plt.show()
