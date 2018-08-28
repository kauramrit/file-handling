#Q.1- Write a Python program to read n lines of a file

f=open('11.txt','r')
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)

#Q.2- Write a Python program to count the frequency of words in a file.

file=open("11.txt","r+")
count={}

for i in file.read().split():
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
for k,v in count.items():
    print(k, v)

#Q.3- Write a Python program to copy the contents of a file to another file

with open("11.txt") as i:
    with open("14.txt", "w") as j:
        for line in i:
            j.write(line)

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('11.txt') as i, open('15.txt') as j:
    for line1, line2 in zip(i, j):
        print(line1+line2)


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

import random
list1=[]
f=open("list.txt","w+")
for i in range(10):
    a=str(random.randint(0,9))
    f.write(a)
f.close()
f=open("list.txt","r")
contents=f.read()
list1=list(contents)
print(list1)
list1.sort()
print(list1)
f=open("new_list.txt","w+")
for i in list1:
    f.write(str(i))
f.close()

