

#   QUESTION :-


#Ramu owns a Pan shop and he manages it in his own way. While in a normal shop, a customer is served by following the first-come, first-served rule, Ramu simply minimizes the average waiting time of his customers. So he gets to decide who is served first, regardless of how sooner or later a person comes.

#Different kinds of Pans take different amounts of time to cook. Also, once he starts cooking a Pan, he cannot cook another Pan until the first Pan is completely cooked. Let's say we have three customers who come at time t=0, t=1, & t=2 respectively, and the time needed to cook their Pans is 3, 9, & 6 respectively. If Ramu applies first-come, first-served rule, then the waiting time of three customers is 3, 11, & 16 respectively. The average waiting time in this case is (3 + 11 + 16) / 3 = 10. This is not an optimized solution. After serving the first customer at time t=3, Ramu can choose to serve the third customer. In that case, the waiting time will be 3, 7, & 17 respectively. Hence the average waiting time is (3 + 7 + 17) / 3 = 9.

#Help Ramu achieve the minimum average waiting time. For the sake of simplicity, just find the integer part of the minimum average waiting time.


#Input Format
#The first line contains an integer N, which is the number of customers.
#In the next N lines, the ith line contains two space separated numbers Ti and Li. Ti is the time when ith customer order a pan and Li is the time required to cook that pan.
#The  ith customer is not the customer arriving at the  ith arrival time. 

#Output Format
#Display the integer part of the minimum average waiting time.
#Note
#The waiting time is calculated as the difference between the time a customer orders pan (the time at which they enter the shop) and the time she is served.
#Cook does not know about the future orders.


import queue
from time import time
from unittest import case
pre_order=[]
last_order=[]
cases=int(input())
available=queue.PriorityQueue(cases)
total_wait=0

for _ in range(cases):
    pre_order.append([int (x) for x in input().split()])
pre_order.sort(key=lambda x: x[0],reverse=True)
last_order=pre_order.pop()
last_order.append(last_order[0] +last_order[1])
total_wait+= last_order[2] - last_order[0]

time=last_order[2]
for _ in range(cases-1):
    while(pre_order and time>=pre_order[-1][0]):
        node=pre_order.pop()
        available.put((node[1],node))
    if available:
        deleted=available.get()[1]
        deleted.append(time + deleted[1])
        total_wait+=deleted[2]- deleted[0]
        last_order=deleted
    else:
        temp =pre_order.pop()
        temp.append(temp[0]+temp[1])
        total_wait+= temp[2] - temp[0]
        last_order=temp
    time=last_order[2]
print(int(total_wait/cases))