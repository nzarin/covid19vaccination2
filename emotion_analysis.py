import math

from nrclex import NRCLex
import pandas as pd
import csv


# def pretty_print():
#     print('\n', text_object.words)
#     print('\n', text_object.sentences)
#     print('\n', text_object.affect_list)
#     print('\n', text_object.affect_dict)
#     print('\n', text_object.raw_emotion_scores)
#     print('\n', text_object.top_emotions)
#     print('\n', text_object.affect_frequencies)
#     print("-----------------------")

def has_no_emotions(affect_frequencies):
    for col in affect_frequencies:
        if affect_frequencies[col] > 0.0:
            return False
    return True


def run_nrclex_analysis(df):
    cols = ['fear', 'anger', 'anticipation', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy']
    df_emotions = pd.DataFrame(columns=cols, index=range(len(df['full_text'])))
    c = 0
    for index, row in df.iterrows():
        text_object = NRCLex(row['full_text'])
        affect_freqs = text_object.affect_frequencies
        print(affect_freqs)
        df_emotions.at[index, 'fear'] = affect_freqs['fear']
        df_emotions.at[index, 'anger'] = affect_freqs['anger']
        df_emotions.at[index, 'anticipation'] = affect_freqs['anticip']
        df_emotions.at[index, 'trust'] = affect_freqs['trust']
        df_emotions.at[index, 'surprise'] = affect_freqs['surprise']
        df_emotions.at[index, 'positive'] = affect_freqs['positive']
        df_emotions.at[index, 'negative'] = affect_freqs['negative']
        df_emotions.at[index, 'sadness'] = affect_freqs['sadness']
        df_emotions.at[index, 'disgust'] = affect_freqs['disgust']
        df_emotions.at[index, 'joy'] = affect_freqs['joy']
        # Check if it has emotions for normalization purposes
        if has_no_emotions(affect_freqs):
            print("Has no emotions, don't increment the counter")
        else:
            c += 1
        print("-----------------------")
    print("Counter value is : {}".format(c))
    result = pd.concat([df, df_emotions], axis=1)
    return result, c


if __name__ == "__main__":
    df_sentences = pd.read_csv('sentiments_only_text_and_score3.csv')
    df_result, counter = run_nrclex_analysis(df_sentences)
    total_fear = math.fsum(df_result['fear']) / counter
    total_anger = math.fsum(df_result['anger']) / counter
    total_anticipation = math.fsum(df_result['anticipation']) / counter
    total_trust = math.fsum(df_result['trust']) / counter
    total_surprise = math.fsum(df_result['surprise']) / counter
    total_positive = math.fsum(df_result['positive']) / counter
    total_negative = math.fsum(df_result['negative']) / counter
    total_sadness = math.fsum(df_result['sadness']) / counter
    total_disgust = math.fsum(df_result['disgust']) / counter
    total_joy = math.fsum(df_result['joy']) / counter
    print("sanity check: all together must equal 1: ")
    print(
        total_fear + total_anger + total_anticipation + total_trust + total_surprise + total_positive + total_negative + total_sadness + total_disgust + total_joy)
    df_result.to_csv('emotion_analysis.csv', index=False)

    # Store summary data
    summary_data = {
        'Emotion': ['fear', 'anger', 'anticipation', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust',
                    'joy'],
        'Score': [total_fear, total_anger, total_anticipation, total_trust, total_surprise, total_positive,
                  total_negative, total_sadness, total_disgust, total_joy]}
    df_summary = pd.DataFrame(summary_data)

    # Write to files
    df_result.to_csv('emotion_analysis.csv', index=False)
    df_summary.to_csv('emotion_analysis_summary.csv', index=False)
