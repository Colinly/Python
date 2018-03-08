def my_shu(a,b,c,*args,**kvs):
	print a,b,c
	print args
	print kvs

my_shu(1,2,3,'hello','world',key = '123',word = 'abc')