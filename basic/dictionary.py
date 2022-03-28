'''d = { 'a':'42', 'b':'32', 'c':'22'}
for i in d.values():
    print(i)
'''
from pickle import NONE
from unittest import result

val1 = {"a":2, "b":3}
val = {'a':'42', 'b':'32', 'c':'22'}
#print(val['a'])
print(val1[1])
result = val.get('d')

if result:
    print(result)
else:
    print("key doesn't exist")

