import numpy
import re
import typing

data = [list(line) for line in open("input/04-test")]
cols = len(data)
rows = len(data[0])
diags: typing.List = []
count = 0
for i in range(-len(data), len(data[0])):
    row = [x for x in "".join(numpy.diagonal(data, offset=i).tolist()) if x != "\n"]
    diags += "".join(f"{row}\n")

data = numpy.rot90(data).tolist()
for i in range(-len(data), len(data[0])):
    row = [x for x in "".join(numpy.diagonal(data, offset=i).tolist()) if x != "\n"]
    diags += "".join(f"{row}\n")

print("".join(diags))
matches = re.findall(r"(XMAS)", "".join([x for x in diags]))
print(matches)
print(len(matches))
