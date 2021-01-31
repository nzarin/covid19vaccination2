from __future__ import absolute_import, print_function

import pandas as pd
import scipy as sc
import numpy as np
import matplotlib as mpl
import csv
from scipy.stats import mannwhitneyu


df = pd.read_csv("task2_data.csv")
df.boxplot(by='relevanceJudge', column=['#entities'], grid=True)
nr_entities_relevant = df[df["relevanceJudge"]==1]["#entities"]
nr_entities_non_relevant = df[df["relevanceJudge"]==0]["#entities"]
print(nr_entities_relevant.describe())
print(nr_entities_non_relevant.describe())
u, p_value = mannwhitneyu(nr_entities_non_relevant, nr_entities_relevant)
print(u)
print(p_value)

mpl.pyplot.show()

