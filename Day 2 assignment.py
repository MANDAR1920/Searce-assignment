
#QUESTION:-


#You have an empty sequence, and you will be given
#queries. Each query is one of these three types:
#1 x  -Push the element x into the stack.
#2    -Delete the element present at the top of the stack.
#3    -Print the maximum element in the stack.

#Function Description
#Complete the getMax function in the editor below.
#getMax has the following parameters:
#- string operations[n]: operations as strings
#Returns
#- int[]: the answers to each type 3 query
# Format
#The first line of input contains an integer,
#. The next
#lines each contain an above mentioned query.
#Constraints
#1<=n<=105
#1<=x<=109
#1<=type<=3



from numpy import append


m=int(input("enter"))
stack=[]
stack_2=[]

for i in range(m):
    data =input().split(' ')
    x=int(data[0])
    v=0

    if len(data)>1: v=int(data[1])
    if x==1:
        stack.append(v)
        if not stack_2 or stack_2[-1]<=v:
            stack_2.append(v)
    elif x==2:
        v=stack.pop()
        if stack_2[-1]==v:
            stack_2.pop()
    else:
        print(stack_2[-1])



