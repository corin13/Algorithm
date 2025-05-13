a = int(input())
b = int(input())

n1 = a*(b%10)
b = b//10
print(n1)

n2 = a*(b%10)
b = b//10
print(n2)

n3 = a*b
print(n3)

print((n1)+(n2*10)+(n3*100))