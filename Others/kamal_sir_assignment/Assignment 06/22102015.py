
start = True	
while start:
	operation =input("choose a operation '+' or '-' or '*' or '/':  ")
	if operation =='+':
		a= int(input('first number: '))
		b=int(input('second number: '))
		print(a+b)
	elif operation =='-':
		a= int(input('first number: '))
		b=int(input('second number: '))
		print(a-b)
	elif operation =='*':
		a= int(input('first number: '))
		b=int(input('second number: '))
		print(a*b)
	elif operation =='/':
		a= int(input('first number: '))
		b=int(input('second number: '))
		print(a/b)
	end = input("type 'no' to stop or type anything to continue:  ")
	if end =='no':
		start=False
		