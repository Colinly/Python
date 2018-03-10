arr = []

def push(element):
	arr.append(element)

def pop():
	if len(arr)<1:
		print "this is a empty arr"
	else:
		print arr[0]
		del(arr[0])

def top():
	if len(arr)<1:
		print "this is a empty arr"
	else:
		print arr[0]
		
push(1)
pop()
push(2)
push(3)
top()
pop()
push(5)
pop()