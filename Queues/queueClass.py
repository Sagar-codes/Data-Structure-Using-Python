import collections
# from collections import deque

q = collections.deque()

# appendleft and POP                          appendLeft --> |30|20|10| --> pop right

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)

print(" Printing deque After AppendLeft: ", q)

q.pop()
q.pop()
q.pop()
q.pop()
print(" Printing deque After POP Right: ", q)

# append and POP left                     popLeft <-- |10|20|30| <-- append right

qu = collections.deque()

qu.append(50)
qu.append(60)
qu.append(70)

print(" Printing deque After AppendRight: ", qu)

qu.popleft()
qu.popleft()
qu.popleft()

print(" Printing deque After POP Left: ", qu)

def is_empty(q):
    if q is not None:
        print("QueueList Is not Empty Print To see the Elements")
        return
    print("Queuelist Is Empty")
is_empty(q)