raw = input("raw = ")

def show(x,raw):
	for i in range(x):
		print(" "),
	for j in range(2*raw-2*x-1):
		print("*"),
	print("\n")

if (raw>3 and raw<21):
	for i in range(raw):
		show(i,raw)
else:
	print "erroe"
		