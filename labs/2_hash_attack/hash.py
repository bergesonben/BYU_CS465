import hashlib
import string
import random

class Hash:
    def __init__(self, inputString, size):
        self.string = inputString
        self.size = size
        self.mask = 0
        for i in range(size):
            self.mask = (self.mask << 1) + 1

    def startAttacks(self):
        self.collisionAttack()
        self.preImageAttack()


    def collisionAttack(self):
        print 'starting collision attack'
        print '========================================================='
        totalCount = 0
        for i in range(100):
            collisionFound = False
            hashes = {}
            count = 0
            while True:
                count = count + 1
                text = self.generateRandomString()
                digest = hashlib.sha1(text).hexdigest()
                digest = self.truncateDigest(digest)
                if (digest in hashes) and (hashes[digest] != text):
                    break;
                hashes[digest] = text
            totalCount += count
            # print 'i = ' + str(i) + ' count = ' + str(count)
            # print 'collision found:'
            # print 'count = ' + str(count)
            # print '\tdigest = ' + digest
            # print '\ttext1 = ' + text
            # print '\ttext2 = ' + hashes[digest]

        print 'avg = ' + str(totalCount / 100)
        # print 'collision found:'
        # print 'count = ' + str(count)
        # print '\tdigest = ' + digest
        # print '\ttext1 = ' + text
        # print '\ttext2 = ' + hashes[digest]

    def preImageAttack(self):
        print '\n\nstarting pre-image attack'
        print '========================================================='
        digest = hashlib.sha1(self.string).hexdigest()
        print 'input = ' + str(self.string)
        print 'actual digest = ' + str(digest)
        digest = self.truncateDigest(digest)
        print 'truncated digest = ' + str(digest)
        totalCount = 0
        for i in range(100):
            collisionFound = False
            count = 0
            while True:
                count = count + 1
                text = self.generateRandomString()
                newDigest = hashlib.sha1(text).hexdigest()
                newDigest = self.truncateDigest(newDigest)
                if digest == newDigest:
                    break
            totalCount += count
        print 'avg = ' + str(totalCount / 100)

    def truncateDigest(self, digest):
        digest = int(digest, 16)
        digest = digest & self.mask
        digest = format(digest, 'x')
        return digest

    def generateRandomString(self):
        numChar = random.randrange(1, 32)
        text = ''
        for i in range(numChar):
            text = text + random.choice(string.printable)
        return text
