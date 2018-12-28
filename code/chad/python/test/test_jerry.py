#!/usr/bin/env python3

data = [
    ["dog", "cat", "horse", "pig", ["test a1", "test a2"]],
    ["cat", "horse"],
]

lists = []

def get_lists(l,s=""):
    y = len(l)-1
    while y >= 0:
        if s == "":
            if isinstance(l[y], list):
                print("list " + str(y) + ": " + str(l[y]))
                lists.append(y)
                get_lists(l[y],y)
        else:
            if isinstance(l[y], list):
                print("list " + str(s) + "," + str(y) + ": " + str(l[y]))
                lists.append([s,y])
                get_lists(l[y],y)
        y -= 1

get_lists(data)
print("lists: " + str(lists))