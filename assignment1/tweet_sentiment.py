import sys
import json

scores = {}

def loadSentimentScores (file):
    for line in file.readlines():
        word, score = line.split ('\t')
        scores[word] = int (score)

def convertFromJson (file):
    for line in file.readlines():
        object = json.loads (line)

        if 'text' in object:
            processTweet (object['text'])

def processTweet (tweet):
    tweetScore = 0
    scoredWords = {}

    for word in tweet.split (' '):
        word = word.lower().encode ('utf-8')
        if word in scores:
            score = scores[word]
            tweetScore += score
            scoredWords[word] = score

    print tweetScore

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    loadSentimentScores (sent_file)
    convertFromJson(tweet_file)

if __name__ == '__main__':
    main()
