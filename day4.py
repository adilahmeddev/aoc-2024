import numpy
import re
from typing import List

data = [list(line) for line in open("input/04")]


def getHorizontalRows(grid: List[List]):
    return ["".join(r + r[::-1] + ["\n"]) for r in grid]


def getDiagRows(grid: List[List]):
    return [
        "".join(
            numpy.diagonal(grid, offset=i).tolist()
            + numpy.diagonal(grid, offset=i).tolist()[::-1]
            + ["\n"]
        )
        for i in range(-len(grid), len(grid[0]))
    ]


rotated = numpy.rot90(data).tolist()
allRows = (
    getHorizontalRows(data)
    + getDiagRows(data)
    + getHorizontalRows(rotated)
    + getDiagRows(rotated)
)


matches = re.findall(r"(XMAS)", "".join([x for x in allRows]))
print(matches)
print(len(matches))
