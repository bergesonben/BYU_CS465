import unittest
from aes import AES

class AESTest(unittest.TestCase):

	def testffAdd(self):
		aes = AES(False)
		self.assertEquals(aes.ffAdd(0x57, 0x83), 0xd4)

	def testxTime(self):
		aes = AES(False)
		self.assertEquals(aes.xtime(0x57), 0xae)
		self.assertEquals(aes.xtime(0xae), 0x47)
		self.assertEquals(aes.xtime(0x47), 0x8e)
		self.assertEquals(aes.xtime(0x8e), 0x07)

	def testffMultiply(self):
		aes = AES(False)
		self.assertEquals(aes.ffMultiply(0x57, 0x13), 0xfe)
		self.assertEquals(aes.ffMultiply(0x02, 0x04), 0x08)
		self.assertEquals(aes.ffMultiply(0x07, 0x0b), 0x31)

	def testSubByte(self):
		aes = AES(False)
		self.assertEquals(aes.subByte(0x53), 0xed)
		self.assertEquals(aes.subByte(0xb4), 0x8d)

	def testSubWord(self):
		aes = AES(False)
		self.assertEquals(aes.subWord(0xcf4f3c09), 0x8a84eb01)
		self.assertEquals(aes.subWord(0x6c76052a), 0x50386be5)
		self.assertEquals(aes.subWord(0x59f67f73), 0xcb42d28f)
		self.assertEquals(aes.subWord(0x7a883b6d), 0xdac4e23c)

	def testRotWord(self):
		aes = AES(False)
		self.assertEquals(aes.rotWord(0xabcdef01), 0xcdef01ab)

	def testKeyExpansion(self):
		aes = AES(False)
		w = aes.keyExpansion(0x2b7e151628aed2a6abf7158809cf4f3c, 4, 10)
		self.assertEquals(w[43], 0xb6630ca6)
		w = aes.keyExpansion(0x8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b, 6, 12)
		self.assertEquals(w[51], 0x01002202)
		w = aes.keyExpansion(0x603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4, 8, 14)
		self.assertEquals(w[59], 0x706c631e)

	def testSubBytes(self):
		aes = AES(False)
		testInput = 0x00102030405060708090a0b0c0d0e0f0
		inputState = aes.toMatrix(testInput)
		testOutput = 0x63cab7040953d051cd60e0e7ba70e18c
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.subBytes(inputState), outputState)

	def testShiftRows(self):
		aes = AES(False)
		testInput = 0x63cab7040953d051cd60e0e7ba70e18c
		inputState = aes.toMatrix(testInput)
		testOutput = 0x6353e08c0960e104cd70b751bacad0e7
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.shiftRows(inputState), outputState)

		testInput = 0x3b59cb73fcd90ee05774222dc067fb68
		inputState = aes.toMatrix(testInput)
		testOutput = 0x3bd92268fc74fb735767cbe0c0590e2d
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.shiftRows(inputState), outputState)

		testInput = 0x36400926f9336d2d9fb59d23c42c3950
		inputState = aes.toMatrix(testInput)
		testOutput = 0x36339d50f9b539269f2c092dc4406d23
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.shiftRows(inputState), outputState)

	def testMixColumns(self):
		aes = AES(False)
		testInput = 0x6353e08c0960e104cd70b751bacad0e7
		inputState = aes.toMatrix(testInput)
		testOutput = 0x5f72641557f5bc92f7be3b291db9f91a
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.mixColumns(inputState), outputState)

		testInput = 0xe8dab6901477d4653ff7f5e2e747dd4f
		inputState = aes.toMatrix(testInput)
		testOutput = 0x9816ee7400f87f556b2c049c8e5ad036
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.mixColumns(inputState), outputState)

		testInput = 0x54d990a16ba09ab596bbf40ea111702f
		inputState = aes.toMatrix(testInput)
		testOutput = 0xe9f74eec023020f61bf2ccf2353c21c7
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.mixColumns(inputState), outputState)

	def testGetKey(self):
		aes = AES(False)
		w = aes.keyExpansion(0x2b7e151628aed2a6abf7158809cf4f3c, 4, 10)
		testOutput = 0xa0fafe1788542cb123a339392a6c7605
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.getKey(w, 1), outputState)

		testOutput = 0xf2c295f27a96b9435935807a7359f67f
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.getKey(w, 2), outputState)

		testOutput = 0x3d80477d4716fe3e1e237e446d7a883b
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.getKey(w, 3), outputState)

	def testAddRoundKey(self):
		aes = AES(self)
		w = aes.keyExpansion(0x2b7e151628aed2a6abf7158809cf4f3c, 4, 10)
		testInput = 0x3243f6a8885a308d313198a2e0370734
		inputState = aes.toMatrix(testInput)
		testOutput = 0x193de3bea0f4e22b9ac68d2ae9f84808
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.addRoundKey(w, 0, inputState), outputState)

		testInput = 0x046681e5e0cb199a48f8d37a2806264c
		inputState = aes.toMatrix(testInput)
		testOutput = 0xa49c7ff2689f352b6b5bea43026a5049
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.addRoundKey(w, 1, inputState), outputState)

		testInput = 0x584dcaf11b4b5aacdbe7caa81b6bb0e5
		inputState = aes.toMatrix(testInput)
		testOutput = 0xaa8f5f0361dde3ef82d24ad26832469a
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.addRoundKey(w, 2, inputState), outputState)

	def testConversion(self):
		aes = AES(False)
		bytes = 0x00102030405060708090a0b0c0d0e0f0
		matrix = [[0x00,0x40,0x80,0xc0],[0x10,0x50,0x90,0xd0],[0x20,0x60,0xa0,0xe0],[0x30,0x70,0xb0,0xf0]]
		self.assertEquals(aes.toMatrix(bytes),matrix)
		self.assertEquals(aes.toBytes(matrix), bytes)

	def testCipher(self):
		debug = True
		aes = AES(debug)
		if debug:
			print '========================================================='
			print 'AES-128 Nk = 4 Nr = 10'
			print 'plaintext = 00112233445566778899aabbccddeeff'
			print 'key = 000102030405060708090a0b0c0d0e0f'
			print 'ENCRYPTION'
			print '========================================================='
		testInput = 0x00112233445566778899aabbccddeeff
		testKey = 0x000102030405060708090a0b0c0d0e0f
		nk = 4
		nr = 10
		testOutput = 0x69c4e0d86a7b0430d8cdb78070b4c55a
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.cipher(testInput, testKey, nk, nr), outputState)

		if debug:
			print '\n\n'
			print '========================================================='
			print 'AES-192 Nk = 6 Nr = 12'
			print 'plaintext = 00112233445566778899aabbccddeeff'
			print 'key = 000102030405060708090a0b0c0d0e0f1011121314151617'
			print 'ENCRYPTION'
			print '========================================================='

		testInput = 0x00112233445566778899aabbccddeeff
		testKey = 0x000102030405060708090a0b0c0d0e0f1011121314151617
		nk = 6
		nr = 12
		testOutput = 0xdda97ca4864cdfe06eaf70a0ec0d7191
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.cipher(testInput, testKey, nk, nr), outputState)

		if debug:
			print '\n\n'
			print '========================================================='
			print 'AES-256 Nk = 8 Nr = 14'
			print 'plaintext = 00112233445566778899aabbccddeeff'
			print 'key = 000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
			print 'ENCRYPTION'
			print '========================================================='

		testInput = 0x00112233445566778899aabbccddeeff
		testKey = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
		nk = 8
		nr = 14
		testOutput = 0x8ea2b7ca516745bfeafc49904b496089
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.cipher(testInput, testKey, nk, nr), outputState)

	def testInvShiftRows(self):
		aes = AES(False)
		testInput = 0x6353e08c0960e104cd70b751bacad0e7
		inputState = aes.toMatrix(testInput)
		testOutput = 0x63cab7040953d051cd60e0e7ba70e18c
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invShiftRows(inputState), outputState)

		testInput = 0x3bd92268fc74fb735767cbe0c0590e2d
		inputState = aes.toMatrix(testInput)
		testOutput = 0x3b59cb73fcd90ee05774222dc067fb68
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invShiftRows(inputState), outputState)

		testInput = 0x36339d50f9b539269f2c092dc4406d23
		inputState = aes.toMatrix(testInput)
		testOutput = 0x36400926f9336d2d9fb59d23c42c3950
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invShiftRows(inputState), outputState)

	def testInvSubBytes(self):
		aes = AES(False)
		testInput = 0x7a9f102789d5f50b2beffd9f3dca4ea7
		inputState = aes.toMatrix(testInput)
		testOutput = 0xbd6e7c3df2b5779e0b61216e8b10b689
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invSubBytes(inputState), outputState)

	def testInvMixColumns(self):
		aes = AES(False)
		testInput = 0x5f72641557f5bc92f7be3b291db9f91a
		inputState = aes.toMatrix(testInput)
		testOutput = 0x6353e08c0960e104cd70b751bacad0e7
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invMixColumns(inputState), outputState)

		testInput = 0x9816ee7400f87f556b2c049c8e5ad036
		inputState = aes.toMatrix(testInput)
		testOutput = 0xe8dab6901477d4653ff7f5e2e747dd4f
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invMixColumns(inputState), outputState)

		testInput = 0xe9f74eec023020f61bf2ccf2353c21c7
		inputState = aes.toMatrix(testInput)
		testOutput = 0x54d990a16ba09ab596bbf40ea111702f
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invMixColumns(inputState), outputState)

	def testInvCipher(self):
		debug = True
		aes = AES(debug)
		if debug:
			print '========================================================='
			print 'AES-128 Nk = 4 Nr = 10'
			print 'plaintext = 00112233445566778899aabbccddeeff'
			print 'key = 000102030405060708090a0b0c0d0e0f'
			print 'DECRYPTION'
			print '========================================================='
		testInput = 0x69c4e0d86a7b0430d8cdb78070b4c55a
		testKey = 0x000102030405060708090a0b0c0d0e0f
		nk = 4
		nr = 10
		testOutput = 0x00112233445566778899aabbccddeeff
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invCipher(testInput, testKey, nk, nr), outputState)

		if debug:
			print '\n\n'
			print '========================================================='
			print 'AES-192 Nk = 6 Nr = 12'
			print 'plaintext = 00112233445566778899aabbccddeeff'
			print 'key = 000102030405060708090a0b0c0d0e0f1011121314151617'
			print 'DECRYPTION'
			print '========================================================='

		testInput = 0xdda97ca4864cdfe06eaf70a0ec0d7191
		testKey = 0x000102030405060708090a0b0c0d0e0f1011121314151617
		nk = 6
		nr = 12
		testOutput = 0x00112233445566778899aabbccddeeff
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invCipher(testInput, testKey, nk, nr), outputState)

		if debug:
			print '\n\n'
			print '========================================================='
			print 'AES-256 Nk = 8 Nr = 14'
			print 'plaintext = 00112233445566778899aabbccddeeff'
			print 'key = 000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
			print 'DECRYPTION'
			print '========================================================='

		testInput = 0x8ea2b7ca516745bfeafc49904b496089
		testKey = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
		nk = 8
		nr = 14
		testOutput = 0x00112233445566778899aabbccddeeff
		outputState = aes.toMatrix(testOutput)
		self.assertEquals(aes.invCipher(testInput, testKey, nk, nr), outputState)

if __name__ == "__main__":
	unittest.main()
