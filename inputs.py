# input a single string in python
i = input("Enter input here: ")
print(i)

# typecast input - replace int with float, bool if required
i = int(input("Enter number here: "))
print(i)

# input list
l=[]
n= int(input("Enter number of elements: "))
for i in range(0, n):
    ele = int(input())
    l.append(ele)
print(l)