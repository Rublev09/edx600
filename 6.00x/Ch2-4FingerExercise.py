integers= []
while len(integers) <10:
	integers.append(int(raw_input('Enter an integer:')))
integers.sort(reverse = True)
oddints=[]
evenints=[]

for num in integers:
        if num % 2!= 0:
                oddints.append(num)
                print num, 'is the largest odd integer you entered'
                break
        elif num % 2 == 0:
                evenints.append(num)
if len(evenints) == len(integers):
                print 'none of the numbers are odd!'


