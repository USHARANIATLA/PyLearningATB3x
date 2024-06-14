# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(), input(), type(), format(), max, min, id(), sum(), avg()

# Strings
name = "Usha"  # 0 to 3
# 0,1,2,3
# U,s,h,a
print(name)
print(type(name))
print(id(name))  # id -> memory address where it is stored 4309895152
print(len(name))
# length of string(1)
# name = name.upper()  -> USHA
# name = name.lower()  -> usha
a = name.count('a')
print(a)
b = name.count('A')
print(b)
# print(name[5]) # string index out of range

# python - Immutable - that can't be changed
# name[0] = "T" # 'str' object does not support item assignment
