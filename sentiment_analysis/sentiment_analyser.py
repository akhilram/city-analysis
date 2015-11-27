__author__ = 'Majisha'

import csv
import argparse
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def main():

    # initialize argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', help='input file')
    parser.add_argument('--output','-o', help='output file')
    args = parser.parse_args()

    sentiment_analyzser = SentimentIntensityAnalyzer()

    businesses = {}

    with open(args.input) as file:
        reader = csv.DictReader(file)
        for row in reader:
            business_id = row['business_id']
            week_id =  row['week']
            tip_text = row['text']
            score = sentiment_analyzser.polarity_scores(tip_text)['compound']
            if score > 0.0:
                tip_value = 1
            elif score < 0.0:
                tip_value = -1
            else:
                tip_value = 0

            try:
                week_aggregate = businesses[business_id]
            except KeyError:
                week_aggregate = {}
                businesses[business_id] = week_aggregate

            try:
                week_aggregate[week_id] += tip_value
            except KeyError:
                week_aggregate[week_id] = tip_value

    with open(args.output, 'w') as file:
        writer = csv.writer(file)
        for business in businesses.keys():
            week_aggregate = businesses[business]
            for week in week_aggregate.keys():
                writer.writerow([business, week, week_aggregate[week]])

    return


#boilerplate for main
if __name__ == '__main__':
    main()

