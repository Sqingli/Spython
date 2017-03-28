
from __future__ import division
print
print
print
for i in range(1,16):
	print("%-13d" %(i)),
for i in range(1,16):
	for j in range(1, i):
		print "%d/%-2d=%-8.3f" %(j, i, j / i),
	print
	print 
	print 
