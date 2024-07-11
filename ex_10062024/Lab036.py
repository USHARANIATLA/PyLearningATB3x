# Practice to print table of a num
"""
for (i==0, i<=10, i++)  # -> SyntaxError: invalid syntax
print(i)

for x in range(10):
print(x=x*2)
"""

n = int(input("Enter the value: "))
i = 1
while i <= 10:
    t = n * i
    print(n, "x", i, "=", t)
    i = i + 1
