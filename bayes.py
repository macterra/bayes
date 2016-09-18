import math

def p2o(prob):
    return prob/(1.-prob)
    
def o2p(odds):
    return odds/(1.+odds)
    
def bayes(prior, factor):
    return o2p(p2o(prior) * factor)

def o2e(odds):
	# evidence in bits
	return math.log(odds)/math.log(2)
    
def e2p(bits):
	return o2p(math.pow(2,bits))
	