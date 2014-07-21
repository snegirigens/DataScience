import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper (record):
    order_id = record[1]
    mr.emit_intermediate (order_id, record)

def reducer (key, list_of_values):
    orderRecords = []
    itemRecords  = []

    for record in list_of_values:
        table = record[0]

        if table == 'order':
            orderRecords.append (record)
        elif table == 'line_item':
            itemRecords.append (record)

    for orderRecord in orderRecords:
        for itemRecord in itemRecords:
            record = list (orderRecord) + list (itemRecord)

            mr.emit (record)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
