
# str, float, int, bool -> immutable -> cannot be changed
# list -> mutable -> can be changed

a = 'Filip'
x = a.upper()

print(f'a: {hex(id(a))}')
print(f'x: {hex(id(x))}')

print(a)
print(x)

print('----------------------')
print('----------------------')

b = 30
y = b
y += 30

print(f'b: {hex(id(b))}')
print(f'y: {hex(id(y))}')

print(b)
print(y)

print('----------------------')
print('----------------------')

f = [1,2,3]
e = f
e.append(12)

print(f'f: {hex(id(f))}')
print(f'e: {hex(id(e))}')


print(f)
print(e)
