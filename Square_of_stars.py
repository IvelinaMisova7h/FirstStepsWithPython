# n = int(input())
# for i in range(1,n+1):
#     print("%s² = %s"%(i,i**2))


n = int(input())

print("*"*n)

for i in range(1, n-1):
    print("*" + " "*(n-2) + "*")

print("*"*n)
