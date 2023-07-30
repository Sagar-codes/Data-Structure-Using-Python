#implement Stack Using List
print("implement Stack Using List")
list_stack = []

list_stack.append(10)
list_stack.append(20)
list_stack.append(30)
print(list_stack) # 1->10, 2->20, 3->30
list_stack.pop()  # 3-> 30 pops out in LIFO or FILO Order
print(list_stack) # 1-> 10 , 2->20

# Implement Stack Using Collections Module
print("Implement Stack Using Collections Module")
import collections

module_stack = collections.deque()
module_stack.append(10)
module_stack.append(20)
module_stack.append(30)
print(module_stack) # 1->10, 2->20, 3->30
module_stack.pop()  # 3-> 30 pops out in LIFO or FILO Order
module_stack.pop()
module_stack.pop()
print(module_stack) 


# Implement Stack Using Queue Module
print("Implement Stack Using Queue Module")
import queue

queue_stack = queue.LifoQueue()

queue_stack.put(10)
queue_stack.put(20)
queue_stack.put(30)
print(queue_stack)
queue_stack.get() # get method pops out in FILO or LIFO
queue_stack.get()
queue_stack.get()
print(queue_stack)

