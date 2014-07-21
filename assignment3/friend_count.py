import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper (record):
    person = record[0]
#    friend = record[1]

    mr.emit_intermediate (person, 1)

def reducer (key, list_of_values):
    count = len (list_of_values)
    mr.emit ((key, count))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
