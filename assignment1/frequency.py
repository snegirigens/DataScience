import sys
import json
import re

totalCount = 0.0
histogram = {}

def processFile (file):
    for line in file.readlines():
        object = json.loads (line)

        if 'text' in object:
            processTweet (object['text'])

def processTweet (tweet):
    for word in tweet.split (' '):
        word = word.lower().encode ('utf-8')
        match = re.search (r"^[\"']?([\w\-']+)[\"']?[,\.!?:]?$", word)
        if not match: continue

        word = match.group (1)

        if word not in histogram:
            histogram[word] = 0

        histogram[word] = histogram[word] + 1
        global totalCount
        totalCount += 1.0

def printHistogram():
    for word in sorted (histogram):
        print "%s %f" % (word, histogram[word] / totalCount)

def main():
    input = open (sys.argv[1])
    processFile (input)
    printHistogram()

if __name__ == '__main__':
    main()
