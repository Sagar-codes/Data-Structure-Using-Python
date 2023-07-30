import queue

# To iterate Queue.Queue items in Python
def print_q(q, m):
    for elem in list(q):
        print(m, elem, end=" ")


q = queue.Queue()  # --> we can put (maxsize) to the queue object. if it is none it takes infine maxsize to the queue.
print(q)

q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(" Printing queue module After put : ", list(q))

q.get()
q.get()
q.get()
q.get()

print(" Printing queue module After get : ", list(q))

