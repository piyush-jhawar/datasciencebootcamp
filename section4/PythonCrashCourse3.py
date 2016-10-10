seq = [1,2,3,4,5]
for i in seq:
    print(i)

i = 1
while i < 5:
    print('i is : {}'.format(i))
    i = i+1


for x in range(10):
    print(x)
#LIst comphrehsension

x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)

print([num**2 for num in x])
def my_func(name):
    print ('Hello '+name)
my_func('Raj')


def square(num):
    """
    THIS IS A DOC STRING
    CAN GO MULTIPLE LINES

    :param num:
    :return:
    """
    return num**2
output = square(4)
print(output)


