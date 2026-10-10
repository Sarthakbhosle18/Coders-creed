Basic syntax
# isEven = lambda x : True if x % 2 == 0 else False
# print (isEven(5))

# isGreater = lambda x,y : "x is greater" if x > y  else "y is greater" if y > x else "both are equal"
# print (isGreater(10,1))

# func = [lambda arg = x : arg*10 for x in range(1,5)]
# for i in func :
#     print(i())

Filter
# c = [1,2,3,4,5,6]
# even = filter (lambda x : x%2 ==0, c)
# print (list(even))

Map
# a = [1,2,3,4,5,6]
# double = map (lambda x : x*2, a)
# print (tuple(double)) 

Reduce
# from functools import reduce
# a=[1,2,3,4,5,6]
# mul = reduce(lambda x,y : x*y, a)
# print(mul)