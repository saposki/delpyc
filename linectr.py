from sys import argv
filename = argv[1]

# print filename
# print type(filename)

fp = open(filename)

L = fp.readlines()
a = []
b = []

for k in L:
     a.append(k.split(' '))

for i in a:
    for j in i:
        b.append(j)
print "Line count -> %r" %(len(L))
print "Word count -> %r" %(len(b))
