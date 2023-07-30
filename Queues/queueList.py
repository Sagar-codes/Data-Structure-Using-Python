#  Queue Implemetion Using List

queueList = []

queueList.append(10)
queueList.append(20)
queueList.append(30)
print(" Printing queueList After Appending List: ", queueList)
print(" Popping", queueList.pop(0)) #10                     #If we Don't Mention Index 0 It will perform Stack
queueList.pop(0) #20
queueList.pop(0) 
print(" Printing queueList After popping 0 from List: ", queueList)

# OR

queueList1 = []

queueList1.insert(0,10)
queueList1.insert(0,20)
queueList1.insert(0,30)
queueList1.insert(0,40)

print(" Printing queueList1 After Inserting List: ", queueList1)

queueList1.pop()
queueList1.pop()
queueList1.pop()

print(" Printing queueList1 After popping from List: ", queueList1)

def is_empty(q):
    if q is not None:
        print("QueueList Is not Empty Print To see the Elements")
        return
    print("Queuelist Is Empty")
is_empty(queueList)