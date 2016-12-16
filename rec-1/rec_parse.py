with open('rec','r') as rec_file:
	cnt=0
	joints=[]
	first=[]
	for line in rec_file:
		line=line.strip('\n')
		args = line.split(',')
		if cnt==0: 
			joints=[joint for joint in args]
			print joints
		elif cnt==1: 
			first=[val for val in args]
			print first

		else:
			print [float(args[i])-float(first[i]) for i in range(len(args))]	

		cnt+=1


with open('deltas','r') as deltas:
	cnt=0
	joints=[]
	first=[]

	for line in deltas:
		line=line.strip('\n')
		args=line.split(',')

		if cnt==0: 
			joints=[joint for joint in args]
			print joints
		else:
			




