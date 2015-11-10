def stdDevOfLengths(L):
	if not L:
		return float('NaN')
	lengths = []
	for strin in L:
		lengths.append(len(strin))
	avg = sum(lengths)/float(len(lengths))
	sqrDiffs = []
	for length in lengths:
		sqrDiffs.append( (length - avg)**2 )
	return ( sum(sqrDiffs) / len(sqrDiffs) )**.5

L2 = ['a', 'z', 'p']
L1 = ['apples', 'oranges', 'kiwis', 'pineapples']

print stdDevOfLengths(L2)
print stdDevOfLengths(L1)

#stdDevOfLengths(L2)
#stdDevOfLengths(L1)

	
