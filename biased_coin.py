from random import random
from bayes import *

TEST = 0.51 # bias threshold
BIAS = 0.52 # actual bias in favor of heads

hBits = 0
tBits = 0
hTotal = 0
tTotal = 0

for i in range(1000):
	x = random()
	heads = x<BIAS
	coin = "H" if heads else "T"
	
	if heads:
		hBits = hBits + o2e(TEST/.5)
		tBits = tBits + o2e((1-TEST)/.5)
		hTotal = hTotal + 1
	else:
		tBits = tBits + o2e(TEST/.5)
		hBits = hBits + o2e((1-TEST)/.5)
		tTotal = tTotal + 1
	hProb = e2p(hBits)
	tProb = e2p(tBits)
	print "%3d %s heads(%3d %.4f %.4f %.4f) tails(%3d %.4f %.4f %.4f)" % (i, coin, hTotal, 1.*hTotal/(i+1), hBits, hProb, tTotal, 1.*tTotal/(i+1), tBits, tProb)
	
	