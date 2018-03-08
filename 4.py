def hanio(n,A,B,C):
	if n == 1:
		print n, A ,"->",B
		
	else:
		hanio (n-1,'A','C','B')
		print n, A ,"->",B
		hanio (n-1,'C','B','A')	
		
hanio(4,'A','B','C')
