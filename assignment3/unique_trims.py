import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper (record):
    sequence_id = record[0]
    nucleotides = record[1]

    nucleotides = nucleotides[:-10]

    mr.emit_intermediate (nucleotides, sequence_id)

def reducer (key, list_of_values):
    mr.emit (key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
