import numpy
import re
import typing
data = [list(line) for line in open('input/04')]
cols = len(data)
rows = len(data[0])
diags: typing.List = []
count = 0
for r in data:
    diags += r + r[::-1]
    diags += '\n'
for i in range(-len(data),len(data[0])):
    row = numpy.diagonal(data, offset=i).tolist()
    diags += row + row[::-1]
    diags += '\n'

data = numpy.rot90(data).tolist()
for r in data:
    diags += r + r[::-1]
    diags += '\n'
for i in range(-len(data),len(data[0])):
    row = numpy.diagonal(data, offset=i).tolist()
    diags += row + row[::-1]
    diags += '\n'


print(''.join([x for x in diags if x!='\n']))

matches = re.findall(r"XMAS", ''.join([x for x in diags if x!= '\n']))
print(len(matches))
