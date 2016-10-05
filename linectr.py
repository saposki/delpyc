from sys import argv
filename = argv[1]

# print filename
# print type(filename)

fp = open(filename)

L = fp.readlines()

a = []
b = []

for k in L:
    check = len(k)
    if check > 1:
        a.append(k.split(' '))
    #  print k

for i in a:
    for j in i:
        b.append(j)

print "Line count -> %r" %(len(a))
print "Word count -> %r" %(len(b))
