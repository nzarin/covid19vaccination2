import pandas as pd
import json
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
from nltk.util import ngrams
from nrclex import NRCLex


for i in range(1,31,1):

    with open("data/US_revised_december{}_december{}.json".format(i, i + 1), 'r') as file:
        data = json.load(file)
        print(len(data))
        x = pd.json_normalize(data['tweets'])
        df = pd.DataFrame(columns=['Text'], index=range(len(x['full_text'])))
        x['full_text'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["", ""], regex=True, inplace=True)
        for j in range(len(x)):
            txt = x.loc[i]["full_text"]
            print("BEFORE ----- BEFORE ---- BEFORE ----")
            print(txt)
            txt = re.sub(r'@[A-Z0-9a-z_:]+','',txt) #replace username-tags
            txt = re.sub('https?://[A-Za-z0-9./]+', '', txt)  # replace URLS
            txt = re.sub("[^a-zA-Z]", " ", txt)  # replace hashtags
            x.at[i, "full_text"] = txt
            print("AFTER ----- AFTER --- AFTER ----")
            print(txt)
            df.append(txt)

    print(df.head(20))

