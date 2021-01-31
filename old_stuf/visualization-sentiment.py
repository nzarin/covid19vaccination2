from __future__ import absolute_import, print_function

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu


df = pd.read_csv("task2_data.csv")
colors = ['red', 'yellow', 'green']
labels = ['negative', 'neutral', 'positive']

nr_relevant = df['relevanceJudge'] == 1
nr_irrelevant = df['relevanceJudge'] == 0

nr_negatives = df['sentiment'] == -1
nr_neutrals = df['sentiment'] == 0
nr_positives = df['sentiment'] == 1

# relevant for us
nr_negative_relevant = df[nr_relevant & nr_negatives]
nr_neutral_relevant = df[nr_relevant & nr_neutrals]
nr_positives_relevant = df[nr_relevant & nr_positives]

nr_negative_irrelevant = df[nr_irrelevant & nr_negatives]
nr_neutral_irrelevant = df[nr_irrelevant & nr_neutrals]
nr_positive_irrelevant = df[nr_irrelevant & nr_positives]

data_negatives = [len(nr_negative_relevant), len(nr_negative_irrelevant)]
data_neutral = [len(nr_neutral_relevant), len(nr_neutral_irrelevant)]
data_positive = [len(nr_positives_relevant), len(nr_positive_irrelevant)]

# from raw value to percentage
r = [0, 1]
totals = [i + j + k for i, j, k in zip(data_negatives, data_neutral, data_positive)]
negs = [i / j * 100 for i, j in zip(data_negatives, totals)]
neuts = [i / j * 100 for i, j in zip(data_neutral, totals)]
pos = [i / j * 100 for i, j in zip(data_positive, totals)]

print(data_negatives)
print(data_neutral)
print(data_positive)

print("-----------------")
nr_entities_relevant = df[df["relevanceJudge"]==1]["sentiment"]
nr_entities_non_relevant = df[df["relevanceJudge"]==0]["sentiment"]
print(nr_entities_relevant.describe())
print(nr_entities_non_relevant.describe())
u, p_value = mannwhitneyu(nr_entities_non_relevant, nr_entities_relevant)
print(u)
print(p_value)

barWidth = 0.85
names = ('Relevant', 'Irrelevant')

# create negative bars
plt.bar(r, negs, color='r', width=barWidth)

# create neutral
plt.bar(r, neuts, color='y', bottom=negs, width=barWidth)

# create positive bars
plt.bar(r, pos, color='g', bottom=[i + j for i, j in zip(negs, neuts)], width=barWidth)

plt.xticks(r, names)
plt.xlabel("Relevance")
plt.legend(labels=['Negatives', 'Neutral', 'Positives'])
plt.show()

