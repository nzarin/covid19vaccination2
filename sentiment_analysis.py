import pandas as pd
import json
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
from nltk.util import ngrams
from nrclex import NRCLex

# open necessary files
with open('data/revised_collection2.json') as f:
    data = json.load(f)

x = pd.json_normalize(data['tweets'])
x['full_text'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["", ""], regex=True, inplace=True)
id_list = []
for i in range(len(x)):
    txt = x.loc[i]["full_text"]
    user_id = x.loc[i]["user.id"]
    if user_id not in id_list:
        id_list.append(user_id)
        print("id list size is now : {}".format(len(id_list)))
    else:
        print("contains already user_id : {}".format(user_id))
    txt = re.sub(r'@[A-Z0-9a-z_:]+', '', txt)  # replace username-tags
    txt = re.sub('https?://[A-Za-z0-9./]+', '', txt)  # replace URLs
    txt = re.sub("[^a-zA-Z]", " ", txt)  # replace hashtags sign
    x.at[i, "full_text"] = txt


def smart_truncate(content, length=256, suffix=''):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix


count = 0
countp = 0
countn = 0
countt = 0
countn1 = 0
countp1 = 0
countt1 = 0
countn2 = 0
countp2 = 0
countt2 = 0
countn3 = 0
countp3 = 0
countt3 = 0

analyzer = SentimentIntensityAnalyzer()
cols = ['Vader', 'TextBlob', 'Sentiment']
df2 = pd.DataFrame(columns=cols, index=range(len(x['full_text'])))

# df_positives = pd.DataFrame(columns=['Score'])
# df_neutrals = pd.DataFrame(columns=['Score'])
# df_negatives = pd.DataFrame(columns=['Score'])

for index, row in x.iterrows():
    vs1 = analyzer.polarity_scores(row['full_text'])['compound']
    vs2 = TextBlob(row['full_text']).sentiment.polarity
    sentence = smart_truncate(row['full_text'])
    print(sentence)
    if vs1 < 0:
        # val1 = -1
        countn1 += 1
    elif vs1 > 0:
        # val1 = 1
        countp1 += 1
    else:
        # val1 = 0
        countt1 += 1
    df2.loc[index].Vader = vs1

    if vs2 < 0:
        val2 = -1
        countn2 += 1
    elif vs2 > 0:
        val2 = 1
        countp2 += 1
    else:
        val2 = 0
        countt2 += 1
    df2.loc[index].TextBlob = vs2

    # weighted vs
    vs = 0.55 * vs1 + 0.45 * vs2

    if vs > 0:
        val = 1
        countp += 1
    elif vs == 0:
        val = 0
        countt += 1
    elif vs < 0:
        val = -1
        countn += 1
    df2.loc[index].Sentiment = vs

    count = count + 1
    if not count % 1000:
        print(count)

stripped_df = x[['created_at', 'full_text', 'user.id']]
df3 = pd.concat([stripped_df, df2], axis=1)

# print('ensemble')
# print('count is : {}'.format(count))
# print('countp is : {}'.format(countp))
# print('countn is : {}'.format(countn))
# print('countt is : {}'.format(countt))

# positive overall average sentiment
print(countp / count)
# negative overall average sentiment
print(countn / count)
# neutral overall average sentiment
print(countt / count)

# handle file writing/closing
df3.to_csv('sentiments_only_text_and_score3.csv', index=False)
