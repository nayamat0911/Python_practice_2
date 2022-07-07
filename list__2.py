a = ['doriamn','shinshun', 67, 'mama']
b = ['tom and jarry', ['foy', 'toy',['roy', 'kaka',["salman","hannan"],'bai'], 'gou'], 'mardok']
print(a)
print(b[1][2])

print(b[:3])
print(a[2:]) # 2 index theke last porjnto
print(b[2][2])
a.append("hey")
print(a)

# for many item add
a.extend(["manik", "jamal" , "hoasin"])  #[] must be outside
print(a)
c = 430
d = 6
f = c*d
print(f)
g = 330

print(f+g*2)
 # append for only one item
 # extend for multiple item

print(len(a))

a.insert(1,4)
print(a)
a.insert(3, 'rasel')
print(a)
# append for add last index but insert for first index add or add index number then , then item
a[2]="doreeemon"
print(a)
a[3]="nayam"
print(a)
print(b)
b[2]=2
print(b)
b[1][3]='now'
print(b)
b[1][2][2]='dada'
print(b)
print(b[1][2][2])
print(b)
del b[1][2][2]
print(b)

print(a)
a.remove('manik')
print(a)
a.pop()
print(a)
a.pop(1)
print(a)

# a.clear(2)
# del a[3]
print(a)

for i in b:
    print(i)

for i in b[1]:
    print(i)

# for i in b[1][1]:
#     print(i)
print("nested list loop print-----------")

for i in b:
    if type(i) is list:
        for j in i:
            if type(j) is list:
                for k in j:
                    print(k)
        else:
            print(j)
    else:
        print(i)


print(b)
print(len(a))
print(len(b))

if "banlga" in a:
    print("paicchi")
else:
    print("nai")
if 'tom and jarry' in b:
    print('paicchi')
else:
    print('nai')

# repitation
print(a*3)
# copy list
h = a.copy()
print(h)
h.append('apple')
print(h)
j = b[1].copy()
print(j)

l=[]
for i in b :
    if type(i) is list:
        l = i.copy()
        print(l)
    else:
        print(i)
print(l)

# concatination

print(b+a)

# index

print(h.index('apple'))

# count
print('cont')
print(h.count('apple'))

#coppy
# reverse
h.reverse()
print(h)

# sort
m =['kakaghdsre', 'mamahhh','dada','fofdgdfgda','khalu', 'baiya']
n = [100,95,1,2,58,8,0,89,]
m.sort()
print(m)

n.sort()
print(n)
print('MAX-----------')
# max
print(max(m))
print(max(n))

# min
print('min----------')
print(min(m))
print(min(n))

print('sum---------------')
print(sum(n))
# print(sum(m))
