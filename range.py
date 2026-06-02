# range(start,stop,step)
# print(range(5))  # range(0,5)

# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])
# print(seq[5])  #error

#Another way
# seq = range(5)
# for i in seq:
#     print(i)

#Printing from 2 to 10
# for i in range(2,10):
#     print(i)

#printing 
# for i in range (2,10,2):
#     print(i)

#Multiplication table for n
n = int(input("enter no. "))
for i in range(1,10):
    print(n*i)