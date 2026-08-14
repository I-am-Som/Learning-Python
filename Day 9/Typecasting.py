a = "45"
b = "98"
print("a =", type(a),"\nb =", type(b))

# explicit type casting --- converting data type of one literal to another data type maunally.  
x = int(a) + int(b)
print(type(x))

print(x)

# explicit type casting --- converting data type of one literal to another data type by Python virtual machine automatically.  
c = 45.12
print(type(c))
d = 56
print(type(d))

y = c+d
print(type(y))

print(y)