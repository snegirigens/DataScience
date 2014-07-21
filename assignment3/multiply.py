import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
dimension = 5

def mapper (record):
    global dimension
    mtx = record[0]
    row = record[1]
    col = record[2]
    val = record[3]

    if mtx == 'a':
        for k in range(dimension):
            mr.emit_intermediate ((row, k), (mtx, col, val))
    else:
        for k in range(dimension):
            mr.emit_intermediate ((k, col), (mtx, row, val))

def reducer (key, list_of_values):
    global dimension
    result = 0
    row = None
    col = None
    A = {}
    B = {}

#    print "Got: key = %s, value = %s" % (key, list_of_values)

    for tuple in list_of_values:
        mtx = tuple[0]
        colrow = tuple[1]
        val = tuple[2]

        if mtx == 'a':
            A[colrow] = val
            row = key[0]
        else:
            B[colrow] = val
            col = key[1]

    for k in range(dimension):
        if k in A and k in B:
            result += A[k] * B[k]

    if row != None and col != None:
        mr.emit ((row, col, result))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
