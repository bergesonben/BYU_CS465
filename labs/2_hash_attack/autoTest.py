import time
from hash import Hash

for i in range(16, 100):
    print '*********************************************************************'
    print 'bits = ' + str(i)
    print '*********************************************************************'
    startTime = time.time()
    myHash = Hash('abc', i)
    myHash.startAttacks()
    endTime = time.time()
    print 'time (in sec) = ' + str(endTime - startTime)
    print '\n\n'
