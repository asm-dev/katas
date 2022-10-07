"""
Print the permutation of lists formed by a, b, && c excluding the arrays that sum to n
"""

# a = int(input())
# b = int(input())
# c = int(input())
# n = int(input())

a = 1
b = 1
c = 1
n = 2


print([[d,e,f] for d in range(a+1) for e in range(b+1) for f in range(c+1) if d+e+f != n])