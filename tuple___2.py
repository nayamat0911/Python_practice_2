a = ("ma","baba","kaka", 34,45)
print(a)
print(type(a))

# tuple data has no option to change data
# tupe tata protected
# constructior
b = tuple(("ma","baba","kaka", 34,45))
print(b)

# tuple megic
c  = " dhaka", "chittagong", 2,4,6
print(c)
print(type(c))

d = ["syllet",('amm','jamm',), "khlna"]
e = ('mango','banena',['jankfurt', 'apple'], 'orenge')
print(d)
print(e)
print(type(d))

d = ("syllet",)

print(d)
print(type(d))
print('type----------')
print(type(d))
print(type(e))

g = ["syllet",'bogora', ('amm','jamm',), "khlna"]
print('index-----------')
print(g[2])
print(g[-2])


print(g[-1:-2])
print(g[-2])
print(g)
kk = ("dhaka", 'comilla','nowakhali', ('bepara','kosba') ,'khulna','jamalpur')
print(kk)

# convert tuple to list
j = list(kk)
print(j)

# then add data in list
j.append('chittagong')
print(j)

# then again convert list to tuple
kk = tuple(j)
print(kk)

# change data in list
j[3]="dinajpur"
print(j)

# convert list to tuple
kk = tuple(j)
print(kk)

# delete data from list
del j[3]
print(j)

# convert list to tuple
kk = tuple(j)
print(kk)
# remove data in tuple via convert tuple to list andt list to tuple
j.remove("dhaka")
kk = tuple(j)
print(kk)

#  clear data from tuple
kk =()
print(kk)
j.append(["kamal",("jaml",'hanif',),'sultan'])
dd = tuple(j)
print(dd)

