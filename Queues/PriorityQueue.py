"""Priority Queues

    Priority Queue are the modified version in which each element is associated with priority and is served according to its priority.
    If elements with same priority occurs they are served according to there order in the queue.

    Methods: 1) Lowest element has highest Priority. 2) Highest element has highest Priority.
    
    Uses : 1) List and 2) Priority Queue Class
"""
#List

q = []

q.append(10)
q.append(20)
q.append(30)
q.sort()  # <--Lowest to highest priority    --> q.sort(reverse=True) Highest to lowest or highest 

print("Printing List Queue using sort priority : ", q)


# Class

#Priority queue class ,  the entries are kept sorted using Heap Queue Model, It uses the Binary Heap Data Structure.

import queue

qq = queue.PriorityQueue()
qq.put(10)
qq.put(20)
qq.put(60)
qq.put(40)
qq.put(40)

print("Priority Class queue", list(qq.queue))


#priority based on tuple and index

qqq = []

qqq.append((1, 'alexa'))
qqq.append((4, 'cortana'))
qqq.append((2, 'python AI'))
qqq.append((3, 'G-Assistant'))
qqq.sort()
print("Tuple Index Sorting Priority: ", qqq)