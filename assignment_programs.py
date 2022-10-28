""" 
#1. Write a program to print all the numbers divisible by 7 but not multiples of 5 from 
# 2000 to 3200

print("All the numbers divisible by 7 but not multiples of 5 from 2000 to 3200: ")

for i in range(2000,3000):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i,end=" ") 
"""


"""
# 2. Write a program which takes N as input and generates a 2-dimensional array of NxN.
#    The element value in the i-th row will be i.
#    Ex:1 1 1
#       2 2 2
#       3 3 3

N = int(input("Enter the value of N: "))

for i in range(1,N+1):
    print(str(i)*N)
"""

"""
#3. Write a program which takes N as input and print the series from 1 till N. It also prints BIZZ if a number is divisible by 3, BUZZ if divisible by 5 and BIZZBUZZ if divisible by both 3 and 5.
#Ex: N=15
#Output: 1
#        2
#        3-BIZZ
#        4
#        5-BUZZ
#        6-BIZZ
#        7
#        8
#        9-BIZZ
#        10-BUZZ
#        11
#        12-BIZZ
#        13
#        14
#        15-BIZZBUZZ

N = int(input("Enter the value of N: "))
for i in range(1,N+1):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i,'-BIZZBUZZ')
    elif (i % 3 == 0):
        print(i,'-BIZZ')
    elif (i % 5 == 0):
        print(i,'-BUZZ')
    else:
        print(i)
"""

"""
# 4. Write a program that accepts a sentence and calculate the number of letters and digits.
#    Suppose the following input is supplied to the program:
#    hello world! 123
#    Then, the output should be:
#    LETTERS 10
#    DIGITS 3

digits = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

sentence = input("Enter the sentence in input: ")
total_digits = 0
total_letters = 0
for s in sentence:
    if s in digits:
        total_digits += 1
    elif s in letters:
        total_letters += 1
    else:
        pass
print("LETTERS: ",total_letters)
print("DIGITS: ",total_digits)
"""


"""
# 5. Write a program that takes n from the user and calculate sum of following series:
#    S= (1) + (1+2) + (1+2+3) + ------+ (1+2+3+4+---+n)
#    Note: Use range() function.

# method 1 (Using for loop): 
n = int(input("Enter the value of n: "))
res = 0

for i in range(1,n+1):
    sum = 0
    if i >1 :
        print("+ (",end=" ")
    else:
        print("(",end=" ")
    for j in range(1,i+1):
        sum += j
        if j == i:
            print(j,end=" ")
        else:
            print(j,'+',end=" ")
    print(")",end=" ")
    res += sum
    
print('=',res)

# method 2 (Using function): 
def sum_of_natural_numbers(num):
    sum = 0
    for i in range(1,num+1):
        if i > 1:
            print("+",end=" ")
        else:
            print("(",end=" ")
        sum += i
        print(i,end=" ")
        if i == num:
            print(")",end=" ")
    return sum
    
n = int(input("Enter the value of n: "))
res = 0
for i in range(1,n+1):
    res += sum_of_natural_numbers(i)
    if i != n:
        print("+",end=" ")

print("=",res)
        
"""