import itertools
ic = int(raw_input("Enter number of items : "))
tc = int(raw_input("Enter number of transactions : "))
msc = int(raw_input("Enter minimum support count : "))
mct=float(raw_input("Enter Minimum Confidence Threshold : "))
trans=[]

for x in range(tc):
	tran=[]
	for y in range(ic):
		temp=int(raw_input())
		tran.append(temp)
	trans.append(tran)

print

#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in trans])) #print the dataset

trans1=[]
for x in range(tc):
	tran1=[]
	for y in range(ic):
		if(trans[x][y]==1):
			tran1.append(y)
	trans1.append(set(tran1))

#print trans1 #final transaction array in required form

L=[]
for l in range(1,ic+1):
	for subset in itertools.combinations(range(ic),l):
		L.append(set(subset))

#print L #All Combination of elements

LC=[]
for l in L:
	lc=0
	for t in trans1:
		if(l.issubset(t)):
			lc+=1
	LC.append(lc)

C=[]
CC=[]
for x in range(len(LC)):
	if(LC[x]>=msc):
		C.append(list(L[x]))
		CC.append(LC[x])

#print LC #Total Count of all elements
#print C
#print CC
print "\nFrequent Elements and corresponding frequencies(L) : "
for x in range(len(C)):
	print "%s : %d"%(C[x],CC[x])
#for x in L:
#	print L[x]+" : "+LC[x]


LHS=[]
RHS=[]
conf=[]

for item in range(len(C)):
	for citem in range(len(C)):
		index=0
		te=list(set(C[item]).union(set(C[citem])))
		if((te in C )and(te != C[item])and(te!=C[citem])and(not(set(C[item])&set(C[citem])))): 
			""""""
			for x in range(len(C)):
				if(te==C[x]):
					index=x
			#print te
			#print index
			temp = float(CC[index])/float(CC[item])
			#print C[index],C[item],CC[index],CC[item],temp
			if(temp>=mct):
				LHS.append(C[item])
				RHS.append(C[citem])
				conf.append(temp)

#print res
#print conf
print "\nAssociation Rules : "
for c in range(len(LHS)):
	print "%s -> %s : %.2f" %(LHS[c],RHS[c],conf[c])
	#print LHS[c]+"->"+RHS[c]+"\t"+conf[c]"""