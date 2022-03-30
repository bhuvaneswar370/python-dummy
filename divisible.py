'''
This challenge got from recurse.com, range of number from 1 to 100, number 3 divisible print crackle
and number 5 divisble print pop, a number is divisible by both number
3 and 5 should get printed cracklepop
'''

for i in range(1,100):
    if i%3 == 0:
        print("crackle",i)
    if i%5 == 0:
        print("pop",i)
    if (i%3 == 0 & i%5 == 0):
        print("CracklePop",i)

 