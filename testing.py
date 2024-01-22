'''
i=1
while i<6:
    print(i)
    i+=1.1
'''
'''
numbers = [0, 254, 2, -1, 3]
for i in numbers:#i is the iteration variable,numbers is the iterable
    if i<0:#if condition not met,execute next level of indentation(print(i) in this case)
        print('Negative number found',i)
        break#escapes the loop, loop will not execute anymore
    print(i)
'''
'''
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
    if i<0:
        continue#do not execute any other code inside the loop,execute the next loop iteration
    print(i)#same level indentation as if,executes if 'if' condition is not met
'''
#while True:
    #pass
'''
n=99
sum=0
while True:
    sum+=n
    n-=1
    if n==0:
        break
print('The sum is:', sum)
'''
#transposed matrix
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(len(matrix[0])):
    transposed1=[]
    for k in matrix:
        transposed1.append(k[i])
    transposed.append(transposed1)
print(transposed)
#To revert to the original matrix
#variable transposed has 4 rows and 2 columns
#for i in range(2) executes first
#k[i] for k in transposed executes second
reverted1=[[k[i] for k in transposed] for i in range(2)]
print(reverted1)

single_digits=[0,1,2,3,4,5,6,7,8,9]
cubes=[i**3 for i in single_digits]
print(cubes)