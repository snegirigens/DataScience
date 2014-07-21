import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper (record):
    person = record[0]
    friend = record[1]

    if (person < friend):
        key = (person, friend)
    else:
        key = (friend, person)

    mr.emit_intermediate (key, (person, friend))

def reducer (key, list_of_values):
    (personA, personB) = key

    if (personA, personB) not in list_of_values or (personB, personA) not in list_of_values:
        mr.emit ((personA, personB))
        mr.emit ((personB, personA))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
