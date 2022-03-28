total = 0
expenses = []
number = int(input("Enter you total number of sum"))
for i in range(number):
    expenses.append(float(input("enter an expense:")))
if 20 in expenses:
    print("The expense list ")
    for j in expenses:
        total = total + j
        print(expenses)
        print("The sum of my expenses Rs",total,sep='') 
else:
    x = sum(expenses)
    print("The sum of my expenses Rs",x,sep='')