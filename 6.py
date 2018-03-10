arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m=3
n=4
arr1 = []



def xuan(list_1,a,b,m,n,list_2):
	if m*n <1:
		return 0
		
	if m*n ==1:
		list_2.append( list_1[a][b])
		return 0
		
	else:
		#up
		if m<1:
			return 0
		else:
			for i in range(n):
				list_2.append(list_1[a][b + i])
				
			
		#down
		if m-1<1:
			return 0
		else:
			for i in range(m-1):
				list_2.append(list_1[a+1+i][b+n-1])
				
		
		#right
		if n-1<1:
			return 0
		else:
			for i in range(n-1):
				list_2.append(list_1[a+m-1][b+n-2-i])
				
		
		#left
		if m-2<1:
			return 0
		else:
			for i in range(m-2):
				list_2.append(list_1[a+m-i-2][b])
				
		xuan(list_1,a+1,b+1,m-2,n-2,list_2)
		
xuan(arr,0,0,m,n,arr1)
print arr1
