import numpy
import re

data = [list(l) for l in open('input/04-test')]
cols = len(data)
rows = len(data[0])
diags = []
count = 0
for i in range(-rows, cols):
    diags += numpy.diagonal(data, offset=i).ravel().tolist()
for r in data:
    count += len(re.findall("XMAS", ''.join(r)))

for i in range(-rows, cols):
    diags += numpy.diagonal(numpy.rot90(data), offset=i).ravel().tolist()

count += len(re.findall("XMAS|SAMX", ''.join(diags)))
print(count)
