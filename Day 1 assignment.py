

    #    QUESTION:-1   


#An array is a data structure that keeps items of the same kind in a single memory block. Each memory position in an array, P, of size Q, has a unique index, I (where 0=i=Q), which may be referred as P[i] or Pi. Reverse an integer array.

#Example 
#P=[4,5,6]
#Return [6,5,4]

#Reverse an integer array. Description of the Function

#complete the reverseArray function in any programming language or your choice or you may write sudo code for the same

#The parameter(s) for reverseArray are:
#int P [q]: the array to reverse  

#Returns
#Int[q]: the reversed array

#Input format
#The first line includes an integer, Q, which represents the number of integers in P.
#P is made up of Q space-separated numbers on the second line.

#Constraints
#1<=Q<=103
#1<=p[i]<=104 where p[i]  is the ith integer in P


#Sample input 

from dataclasses import dataclass


5
8
7
6
#Sample output
6
7
8
5



# Method 1: using sliced string

arr=[1,2,3,4,5]
print("array is:",arr)

res=arr[::-1]
print("reversed array:",res)

# **********************************************************************************************************

# Method 2: Without using inbuilt function

numbers=[1,2,3,4,5,6,7]
L=len(numbers)
for i in range(int(L/2)):
    n=numbers[i]
    numbers[i]=numbers[L-i-1]
    numbers[L-i-1]=n
print(numbers)



# **********************************************************************************************************



#   QUESTION N0:-2

#This is a good way to get some practise with traversing a linked list. Print each node's data element, one per line, given a pointer to the head node of a linked list. There is nothing to output if the head reference is null (meaning the list is empty).


#Create a function to print LinkedLists.
#The parameter(s) for printLinkedList are as follows:
#SinglyLinkedList The head of the list is referred to as the node head.
#Print the value of each node in a new line

#Input format
#The first line of input contains p, which is the number of linked list entries. The data values for each node are contained in the next p lines, each with one element.


#Complete the  printlinkedlist  in any programming language or your choice or you may write sudo code for the same

#Constraints
#1<=P<=1000
#1<=list[i]<=1000 where list [i] is the ith element of the linked list



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end='')
            current=current.next
a_list=LinkedList()
n=int(input("how many elements would you like to add"))
for i in range(n):
    data=int(input('enter data item:'))
    a_list.append(data)
print("the linked list is:",end='')
a_list.display()

