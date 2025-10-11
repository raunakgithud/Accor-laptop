#assesment

#x = [1, 2, 3]
#y = x[:]
#y.append(4)
#print(x, y)
#

#x = 10
#y = 20
#x, y = y, x + y
#print(x, y)
#

#def func(nums=[]):
#    nums.append(len(nums))
#    return nums
#
#print(func())
#print(func())
#
#x = 5
#def outer():
#    x = 10
#    def inner():
#        nonlocal x
#        x += 1
#        return x
#    return inner()
#
#print(outer())
#

#s = "Python"
#print(s[::-2])
#
#
#x = [1, 2, 3]
#y = (x, )
#x.append(4)
#print(y)
#

#from collections import defaultdict
#
#d = defaultdict(int)
#d['a'] += 1
#print(d)
#

#x = {1, 2, 3}
#y = {3, 4, 5}
#print(x & y, x | y, x - y)
#
#
#class A:
#    def __init__(self):
#        self.x = 1
#
#class B(A):
#    def __init__(self):
#        super().__init__()
#        self.x += 1
#
#obj = B()
#print(obj.x)
#

