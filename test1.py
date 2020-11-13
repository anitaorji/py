letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'c']
print (letters , letrs)

names = ['favour' , 'rita' , 'gina']
# idx [for k, v in enumerate(names) if v== 'rita' ]
print ('index = ' + str(idx[0]))

my_stack = Stack()
my_stack.push(4)
my_stack.push(5)
print (my_stack)
print (my_stack.pop())
print (my_stack.peek())

from collections import deque
my_queue = deque()
my_queue.append(9)
my_queue.append(5)
my_queue.append(7)
my_queue.append(2)
print (my_queue)
print (my_queue.popleft(9))

m = MaxHeap ([95,3,31])
m.push(10)
print(m)
print (m.pop())
print (m.peek())

edges = ['AB' , 'AE' , 'BF' , 'CG' , 'DE' , 'DH' 'EH' , 'FG' , 'FI' , 'FJ' 'GJ']
for egdes in edges:
    g.add.edge(edge[0] , edge[1])

g.print_graph() 