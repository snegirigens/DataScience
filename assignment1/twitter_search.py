import oauth2 as oauth
import urllib2 as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "TfII1oe6DpiFuU8pMHPIhssJ6"
api_secret = "aQnjyA1Rbc976fktKa65PPiCtQSFbrbu0VN6JundCPCbeijMBA"
access_token_key = "186781602-EevCi3Rft64QhcVPzJJRx6hj35xhctJoeMBvmP8T"
access_token_secret = "zqfZ0TBIWZw9tKjxccyK7UDcTsrOqXoxf8Ypvm0UJY6bG"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def convertFromJson (response):
    for line in response:
        object = json.loads (line)

        if 'statuses' in object:
            statuses = object['statuses']
            for tweet in statuses:
                if 'text' in tweet:
                    print tweet['text']

def fetchsamples():
    # url = "https://stream.twitter.com/1/statuses/sample.json"

    term = 'vacation'
    url = u"https://api.twitter.com/1.1/search/tweets.json?q=" + term
    parameters = []
    response = twitterreq(url, "GET", parameters)

    convertFromJson (response)

    # for line in response:
    #     print line.strip()

if __name__ == '__main__':
  fetchsamples()
