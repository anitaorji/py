x = 'frog'
print (x[3])

a = 'horse' + 'men'
print (a)

y = [8, 5] * 3
print (y)

y = ['pig' , 'goat' , 'cow']
print (sorted(y))

e = [56 , 72 ,12]
print (min(e))
print (max(e))
print (len(e))


r = ['king' , 'queen' , 'heir']
for item in r:
    print (r)

g = ['tree' ,'tea' ,'hat', 'jug']
a,c,b,d = g
print (a,c,b,d)

y = [m for m in range (5)]
print (y)

t = [m**3 for m in range (8)]
print (t)

w = [9 , 6 , 7 , 4]
w.append(67)
print (w)

w = [9 , 6 , 7 , 4]
x = (67 , 54)
w.extend(x)
print (w)
print (sorted(w))

w = [9 , 6 , 7 , 4]
w.insert(2 , 8)
print (w)

p = [34,56,67]
p.pop()
print (p) 
print (p.pop())
print (p.pop())

y = [45,56,67,34,56,]
y.remove(56)
print (y)

x = ()
x = 2,
print (x ,type(x))

x = ()
x = 2
print (x ,type(x))

y = ([1,2], 5)
del(y[0][0])
print (y)

y = ([1,2], 5)
y += (4,)
print (y)

u = {6,7,6,7}
print (u)

d = {6,4,2}
d.add (5)
print (d)
d.remove (4)
print (d)
print (5 in d)

set1 = {9,8,3}
set2 = {6,9,2}
print (set1 >= set2)
print (set2 >= set1)
print (set1 <= set2)
print (set2 <= set1)
print (set1 & set2)
print (set1 | set2)
print (set1 ^ set2)
print (set1 - set2)

e = { 'real' : '34.5' , 'peak' : '45.63'}
e['shrimp'] = 34.7
print (e)
del(e['shrimp'])
print (e)
print (e.keys())
print (e.values())
print (e.items())

under_12 = [x for x in range(12)]
print ('under_12: ' + str(under_12))

squares = [x**2 for x in under_12]
print ('squares: ' + str(squares))

odds = [x for x in range(12) if x % 2]
print ('odds: ' + str(odds))

five_x = [x * 10 for x in under_12]
print ('five_x: ' + str(five_x))

h = 'she 1s a g00d g1rl 4 real'
nos = [x for x in h if x.isnumeric()]
print ('nos: ' + ''.join(nos))

a = [[1,2] , [3,4]]
new_lists = [x for b in a for x in b]
print(new_lists)

nums = [3,45,7,9,86]
new_list = [x if x%2 == 0 else 10*x for x in nums]
print ('new list: ' + str(new_list))

my_stack = list()
my_stack.append(4)
my_stack.append(56)
print (my_stack)
my_stack.append(9)
my_stack.append(34)
print (my_stack)



