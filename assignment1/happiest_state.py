import sys
import json

scores = {}
statesByCoords = {}
setats = {}     # State name : state code
stateScores = {}

def loadSentimentScores (file):
    for line in file.readlines():
        word, score = line.split ('\t')
        scores[word] = int (score)

def loadStatesInfo():
    for code in states:
        setats[states[code]] = code

    for state in usBB:
        boundingbox = usBB[state]
        box = [float (boundingbox[0]), float (boundingbox[1]), float (boundingbox[2]), float (boundingbox[3])]
        corner = box[0] + box[1]
        statesByCoords[corner] = (box, state)

    # for line in file.readlines():
    #     object = json.loads (line)
    #     object = object[0]
    #     display_name = object['display_name']
    #     boundingbox  = object['boundingbox']
    #
    #     box = [float (boundingbox[0]), float (boundingbox[1]), float (boundingbox[2]), float (boundingbox[3])]
    #     corner = box[0] + box[1]
    #     statesByCoords[corner] = (box, display_name)

def processFile (file):
    for line in file.readlines():
        object = json.loads (line)

        if 'text' in object:
            score = processTweet (object['text'])
            state = processLocation (object)

            if state != None:
                state = setats[state]
                if state not in stateScores:
                    stateScores[state] = 0

                stateScores[state] += score
#                print "%s = %d. %s" % (state, score, object['text'])

def processTweet (tweet):
    tweetScore = 0
    scoredWords = {}

    for word in tweet.split (' '):
        word = word.lower().encode ('utf-8')
        if word in scores:
            score = scores[word]
            tweetScore += score
            scoredWords[word] = score

    return tweetScore

def processLocation (tweet):
    if tweet['place'] != None:
        place = tweet['place']
        country_code = place['country_code']

        if country_code == 'US':
            return processUSLocation (tweet)

    return None

def processUSLocation (tweet):
    if tweet['coordinates'] != None:
        stateTuple = getStateByCoords (tweet['coordinates']['coordinates'])
        if stateTuple != None:
            state = stateTuple[1].split (',')[0]
            return state

    return None

def getStateByCoords (coords):
    lat = coords[1]
    lon = coords[0]

    for corner in statesByCoords:
        box = statesByCoords[corner][0]

        if lat >= box[0] and lat <= box[1] and lon >= box[2] and lon <= box[3]:
            return statesByCoords[corner]

    return None

def byValue (key):
    return stateScores.get (key)

def printStates():
    for state in sorted (stateScores, key=byValue, reverse=True):
        print state
#        print state + " " + str (stateScores[state])
        break

def main():
    dir = sys.argv[0].split('/')
    dir.pop()
    curdir = '/'.join (dir)

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # states_file = open (curdir + '/US-bb.txt')

    loadSentimentScores (sent_file)
    loadStatesInfo()
    # loadStatesInfo (states_file)
    processFile (tweet_file)
    printStates()

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

usBB = {
    "Alabama, United States of America" : ["30.1375217437744","35.0080299377441","-88.4731369018555","-84.8882446289062"],
    "Arizona, United States of America" : ["31.3321762084961","37.0042610168457","-114.818359375","-109.045196533203"],
    "Arkansas, United States of America" : ["33.0041046142578","36.4996032714844","-94.6178131103516","-89.6422424316406"],
    "California, United States of America" : ["32.5295219421387","42.0095024108887","-124.482009887695","-114.13077545166"],
    "Colorado, United States of America" : ["36.9924240112305","41.0023612976074","-109.060256958008","-102.041580200195"],
    "Connecticut, United States of America" : ["40.9667053222656","42.0505905151367","-73.7277755737305","-71.7869873046875"],
    "Delaware, United States of America" : ["38.4511260986328","39.8394355773926","-75.7890472412109","-74.9846343994141"],
    "Florida, United States of America" : ["24.3963069915771","31.0009689331055","-87.6349029541016","-79.9743041992188"],
    "Georgia, United States of America" : ["30.3557567596436","35.0008316040039","-85.6051712036133","-80.7514266967773"],
    "Idaho, United States of America" : ["41.9880561828613","49.000846862793","-117.243034362793","-111.043563842773"],
    "Illinois, United States of America" : ["36.9701309204102","42.5083045959473","-91.513053894043","-87.0199203491211"],
    "Indiana, United States of America" : ["37.7717399597168","41.7613716125488","-88.0997085571289","-84.7845764160156"],
    "Iowa, United States of America" : ["40.3755989074707","43.5011367797852","-96.6397171020508","-90.1400604248047"],
    "Kansas, United States of America" : ["36.9930801391602","40.0030975341797","-102.0517578125","-94.5882034301758"],
    "Kentucky, United States of America" : ["36.4967155456543","39.1474609375","-89.5715103149414","-81.9645385742188"],
    "Louisiana, United States of America" : ["28.9210300445557","33.019458770752","-94.0431518554688","-88.817008972168"],
    "Maine, United States of America" : ["42.9561233520508","47.4598426818848","-71.0841751098633","-66.9250717163086"],
    "Maryland, United States of America" : ["37.8856391906738","39.7229347229004","-79.4871978759766","-75.0395584106445"],
    "Massachusetts, United States of America" : ["41.1863288879395","42.8867149353027","-73.5081481933594","-69.8615341186523"],
    "Michigan, United States of America" : ["41.6960868835449","48.3060646057129","-90.4186248779297","-82.122802734375"],
    "Minnesota, United States of America" : ["43.4994277954102","49.3844909667969","-97.2392654418945","-89.4833831787109"],
    "Mississippi, United States of America" : ["30.1477890014648","34.9960556030273","-91.6550140380859","-88.0980072021484"],
    "Missouri, United States of America" : ["35.9956817626953","40.6136360168457","-95.7741470336914","-89.0988388061523"],
    "Montana, United States of America" : ["44.3582191467285","49.0011100769043","-116.050003051758","-104.039558410645"],
    "Nebraska, United States of America" : ["39.9999961853027","43.0017013549805","-104.053520202637","-95.3080520629883"],
    "Nevada, United States of America" : ["35.0018730163574","42.0022087097168","-120.005729675293","-114.039642333984"],
    "New Hampshire, United States of America" : ["42.6970405578613","45.3057823181152","-72.55712890625","-70.534065246582"],
    "New Jersey, United States of America" : ["38.7887535095215","41.3574256896973","-75.5633926391602","-73.8850555419922"],
    "New Mexico, United States of America" : ["31.3323001861572","37.0001411437988","-109.050178527832","-103.000862121582"],
    "New York, United States of America" : ["40.4773979187012","45.0158615112305","-79.7625122070312","-71.8527069091797"],
    "North Carolina, United States of America" : ["33.7528762817383","36.5880393981934","-84.3218765258789","-75.4001159667969"],
    "North Dakota, United States of America" : ["45.9350357055664","49.0004920959473","-104.049270629883","-96.5543899536133"],
    "Ohio, United States of America" : ["38.4031982421875","42.3232383728027","-84.8203430175781","-80.5189895629883"],
    "Oklahoma, United States of America" : ["33.6191940307617","37.0021362304688","-103.002571105957","-94.4312133789062"],
    "Oregon, United States of America" : ["41.9917907714844","46.2991027832031","-124.703544616699","-116.463500976562"],
    "Pennsylvania, United States of America" : ["39.7197647094727","42.5146903991699","-80.5210876464844","-74.6894989013672"]
}

if __name__ == '__main__':
    main()
