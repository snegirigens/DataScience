import sys
import json

scores = {}
termScores = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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
    scoredTweet = False

    for word in tweet.split (' '):
        word = word.lower().encode ('utf-8')
        if word in scores:
            score = scores[word]
            tweetScore += score
            scoredTweet = True

    if scoredTweet:
        for word in tweet.split (' '):
            word = word.lower().encode ('utf-8')
            if word not in scores:
                if word in termScores:
                    wordScore, totalTweets = termScores[word]
                else:
                    wordScore, totalTweets = [0, 0]

                termScores[word] = [wordScore + tweetScore, totalTweets + 1]
#                print "%s: score = %d; count = %d" % (word, termScores[word][0], termScores[word][1])

#    if tweetScore != 0:
#        print str (tweetScore) + ". " + tweet
#    print tweetScore

def printTermSentiments():
    for word in termScores:
        print "%s %f" % (word, termScores[word][0]/termScores[word][1])


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    loadSentimentScores (sent_file)
    convertFromJson(tweet_file)
    printTermSentiments()

    # hw()
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
