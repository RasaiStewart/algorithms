# Programming dijkstra

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
''' Nahid '''

import pdb

import pandas as pd
import os
import tkinter as tk

pdb.set_trace()
class Node:
    def __init__(self, name:str, time:float):
        self.name = name
        self.time = time
        self.nodes = []
    def addNode(self, node:Node):
        if node is None:
            return
        if node not in self.nodes:
            self.nodes.append(node)
    


class LinkedList:
    def __init__(self):
        self.nodes = []
    def addNode(self, node: Node):
        if node is None:
            return
        if node not in self.nodes:
            self.nodes.append(node)
    
    def getMinCost(self, src: Node, dest: Node):
        if src is not None and dest is not None:
            cost= 0.0
            start = True
            found = False
            for node in self.nodes:
                if (node == src or node == dest) and start is False:
                    start = True
                    continue
                if start == True:
                    # find the next nodes
                    cost = cost + node.time
                    if dest == node:
                        print("cost is: ", cost)
                        found = True
                        break
                    if src == node:
                        print("cost is: ", cost)
                        found = True
                        break
            else:
                if found == False:
                    print("Time not found: ")
                    return
                print("Total cost: ", cost)



'''ll = LinkedList()
n1 = Node("n1", 0.0)
n2 = Node("n2", 3.0)
n3 = Node("n3", 1.0)
ll.addNode(n1)
ll.addNode(n2)
ll.addNode(n3)

ll.getMinCost(n1, n3)'''
df = pd.read_excel("London Underground data.xlsx")

columns = ['location','source', 'destination', 'time']
df.columns = columns
print("London Underground data...")
print(df.head())

print("Formatted data...")
df = df.dropna(axis=0)
print(df.head())


#plot.plot(df['source'], df['time2'])

# create the dictionary linking sources to destinations

links = {}

for x in range(0,len(df)):
    row = df.iloc[x]
    source = row['source']
    destination = row['destination']
    time = row['time']
    joined = str(source)+"_"+str(destination)
    joined = joined.lower()
    if joined not in links:
        links[joined] = time
    else:
        if links[joined] == time:
            continue
        else:
            print("Data error, found different values: ")

else:
    for i in links:
        print(i, end=" ")
        print(links[i])


'''Show a table for the stations and the time needed to travel'''
mydata = {}
mydata['Source'] = []
mydata['Destination'] = []
mydata['Time'] = []
for i in links:
    stations = i.split("_")
    time = links[i]
    mydata['Source'].append(stations[0])
    mydata['Destination'].append(stations[1])
    mydata['Time'].append(time)
    #print(stations[0],"  ", stations[1], "  ", links[i])

tosavedf = pd.DataFrame(mydata)
tosavedf.to_excel("output.xlsx")
print("Finished saving to output.xlsx")

os.startfile("output.xlsx")


'''This part now allows searching a source and destination stations and outputing
the time it takes'''

def search(source : str, destination : str):
    print(f"Searching the time from {0} to {1}...", source, destination)
    source = source.lower().strip()
    destination = destination.lower().strip()
    for x in range(0, len(tosavedf)):
        row = tosavedf.iloc[x]
        src = row['Source']
        src = str(src).lower()
        dest = row['Destination']
        dest = str(dest).lower()
        if src == source:
            if dest == destination:
                #found a match
                print("Time from ",source, " to ", destination, " is ", row['Time']," seconds")
                return row['Time']
    
    return None


def main():
    stop = False
    print("\n...............................................")
    while not stop:
        print("London Underground System\nPress:\n1) any key to continue\n0) 0 to Exit")
        choice = str(input("Select an option: "))
        if choice == "0":
            print("Thank you for using our services. Sad to see you leave :(")
            stop =True
            break
        src = input("Enter the source station: ")
        dest = input("Enter the destination station: ")
        
        time = search(src, dest)
        if time is None:
            print(f"The time from {0} to {1} is not determined", src, dest)

        print("\n\n...............................................")


if __name__=="__main__":
    main()
