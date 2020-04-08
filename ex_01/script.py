#! /usr/bin/env python3
import sys
compteur = 0
iterParam = iter(sys.argv)
next(iterParam)
for i in iterParam:
    for ii in i:
        if ii.isalnum():
            compteur = compteur + 1
print(compteur)
