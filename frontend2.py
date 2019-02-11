import backend
import sys

r = open(sys.argv[1], "r")
w = open(sys.argv[2], "w+")

for l in r:
	w.write(backend.solve(l.split(' ')))
	w.write("\n")
