import subprocess
import numpy
import csv


# Run the other script
subprocess.run("python3", "scraper.py")

pokeStops = {}

# reading in the csv file for data manipulation
with open('pokeStops.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    indexCount = 1
    for row in spamreader:
        if (row != []):

            # sanitizes the csv input
            if (row[1][1] == '-'):
                row[1] = float(row[1][2:])
            else:
                row[1] = float(row[1][1:])
            if (row[2][1] == '-'):
                row[2] = float(row[2][1:-1])
            else:
                row[2] = float(row[2][0:-1])

            # storing the data in the pokeStops dictionary
            pokeStops[indexCount] = {"name": row[0],
                                     "x": row[1], "y": row[2], "selected": False, "weights": {}}
            indexCount += 1

# gathering each weight (represented in distance) for each node in on the map
for i in pokeStops:
    tempX = pokeStops[i]['x']
    tempY = pokeStops[i]['y']
    for j in pokeStops:
        if (j == i):
            continue
        distance = numpy.sqrt(
            (tempX - pokeStops[j]['x'])**2 + (tempY - pokeStops[j]['y'])**2)
        pokeStops[i]["weights"][j] = distance

# prims algorithm to construct a minimum spanning tree
mst = []
for i in range(len(pokeStops)):
    mst.append([])

edges = 0

while (edges < len(pokeStops)):

    minimum = 1000000
    minX = 0
    minY = 0
    for i in range(len(pokeStops)):
        if (pokeStops[i]["selected"]):
            for j in range(len(pokeStops)):
                if (pokeStops[j]["selected"] == False):
                    if (pokeStops[i]["weights"][j] < minimum):
                        minimum = pokeStops[i]["weights"][j]
                        minX = i
                        minY = j
    mst[minX].append(minY)
    pokeStops[minY]["selected"] = True
    edges += 1

queue = [0]
while len(queue) != 0:
    front = queue[0]
    print(pokeStops[front]["name"])
    for i in mst[front]:
        if (i != 0):
            queue.append(i)
    queue.pop(0)
