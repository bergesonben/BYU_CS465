import argparse
from hash import Hash

parser = argparse.ArgumentParser(description='hashAttack Manual Test')
parser.add_argument('-n', metavar='bits', required=False, help='number of bits', default=10)
parser.add_argument('string')

args = parser.parse_args()
bits = int(args.n)
inputString = args.string

myHash = Hash(inputString, bits)
myHash.startAttacks()
