#Lambda Expression
#map and filter

def times2(var):
    return var*2
print(times2(2))

#map()
seq = [1,2,3,4,5]
print(list(map(times2,seq)))


print(list(map(lambda var:var*3,seq)))

#filter function

print(list(filter(lambda num : num%2 == 0,seq)))
s = 'Hello my name is Sam'
print(s.lower())
print(s.split())

d = {'k1':1,'k2':2}
print(d.keys())
print(d.items())
print(d.values())
print(d.pop('k1'))

list = [1,2,3]
print(list.pop())

print('x' in [1,2,3,4])

#Tuple Unpacking
x = [(1,2),(3,4),(5,6)]
print(x[0])
print()
for item in x:
    print(item)

for a,b in  x:
    print(a,b)





