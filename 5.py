#arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#m=3
#n=4
m = int(raw_input('>'))
n = int(raw_input('>'))
arr = [[0]*n for i in range(m)]

def xuan(list_1,a,b,m,n,start):
	if m*n <1:
		return 0
		
	if m*n ==1:
		list_1[a][b] = start
		return 0
		
	else:
		#up
		if m<1:
			return 0
		else:
			for i in range(n):
				list_1[a][b + i] = start
				start +=1
			
		#down
		if m-1<1:
			return 0
		else:
			for i in range(m-1):
				list_1[a+1+i][b+n-1] = start
				start+=1
		
		#right
		if n-1<1:
			return 0
		else:
			for i in range(n-1):
				list_1[a+m-1][b+n-2-i] = start
				start+=1
		
		#left
		if m-2<1:
			return 0
		else:
			for i in range(m-2):
				list_1[a+m-i-2][b] = start
				start +=1
		xuan(list_1,a+1,b+1,m-2,n-2,start)
		
xuan(arr,0,0,m,n,1)
print arr

for i in range(m):
	print arr[i]