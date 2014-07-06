import sys
import json

hashtags = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def byValue (key):
    return hashtags.get (key)

def proceedFile (file):
    for line in file.readlines():
        object = json.loads (line)
        if 'text' not in object: continue
        if 'entities' not in object: continue

        entities = object['entities']

        for hashtag in entities['hashtags']:
            text = hashtag['text']
            if text not in hashtags:
                hashtags[text] = 0

            hashtags[text] += 1

def printHashtags (count):
    for hashtag in sorted (hashtags, key=byValue, reverse=True):
        if count <= 0: break
        print hashtag + " " + str (hashtags[hashtag])
        count -= 1


def main():
    tweet_file = open(sys.argv[1])

    proceedFile(tweet_file)
    printHashtags (10)

if __name__ == '__main__':
    main()
