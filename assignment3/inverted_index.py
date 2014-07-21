import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper (record):
    # key: document identifier
    # value: document contents
    docid = record[0]
    text  = record[1]

    for word in text.split():
      mr.emit_intermediate (word, docid)

def reducer (key, list_of_values):
    # key: word
    # value: list of document ids
    docs = {}

    for docid in list_of_values:
      docs[docid] = None

    mr.emit ((key, docs.keys()))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
