num1 = input("Input a number: ")
num1 = int(num1) #cast to an int

num2 = input("Input another number: ")
num2 = int(num2) #cast to an int

small = min(num1,num2)
large = max(num1,num2)

for i in range(small, large + 1, 1):
	print(i)
