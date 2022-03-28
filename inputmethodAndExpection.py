

"""
This is the multi line comment
"""
x= input("Enter value x\t")
# Here the input read string, we want to enter a number need explict convert into integer
y= input("Enter value y\t")
z = None
try:
    z = int(x) + int(y)
    print(f"The sum of {x} and {y} is {z}")
except ValueError as e:
    print("Enter interger value")


#This is the older format
#print("The sum of {0} and {1} is {2}".format(x,y,z))

